-- taxonomia — recria assuntos e subassuntos com familia_id na posição correta
--
-- Ordem das colunas:
--   assuntos:    assunto_id, disciplina_id, familia_id, name, ordem, ativo
--   subassuntos: subassunto_id, assunto_id, familia_id, name, ordem, ativo
--
-- Um único comando DO (evita o SQL Editor do Supabase executar CREATE e INSERT
-- em conexões diferentes, o que gera "relation does not exist").

do $mig$
begin
  drop table if exists taxonomia.subassuntos_new;
  drop table if exists taxonomia.assuntos_new;

  create table taxonomia.assuntos_new (
    assunto_id    text    primary key,
    disciplina_id text    not null,
    familia_id    text    not null,
    name          text    not null,
    ordem         integer not null,
    ativo         boolean not null default true,
    constraint assuntos_disciplina_id_fkey
      foreign key (disciplina_id) references taxonomia.disciplinas (disciplina_id),
    constraint assuntos_familia_id_fkey
      foreign key (familia_id) references taxonomia._familias (familia_id)
  );

  insert into taxonomia.assuntos_new (assunto_id, disciplina_id, familia_id, name, ordem, ativo)
  select
    a.assunto_id,
    a.disciplina_id,
    d.familia_id,
    a.name,
    a.ordem,
    a.ativo
  from taxonomia.assuntos a
  join taxonomia.disciplinas d on d.disciplina_id = a.disciplina_id;

  create table taxonomia.subassuntos_new (
    subassunto_id text    primary key,
    assunto_id    text    not null,
    familia_id    text    not null,
    name          text    not null,
    ordem         integer not null,
    ativo         boolean not null default true,
    constraint subassuntos_assunto_id_fkey
      foreign key (assunto_id) references taxonomia.assuntos_new (assunto_id),
    constraint subassuntos_familia_id_fkey
      foreign key (familia_id) references taxonomia._familias (familia_id)
  );

  insert into taxonomia.subassuntos_new (subassunto_id, assunto_id, familia_id, name, ordem, ativo)
  select
    s.subassunto_id,
    s.assunto_id,
    n.familia_id,
    s.name,
    s.ordem,
    s.ativo
  from taxonomia.subassuntos s
  join taxonomia.assuntos_new n on n.assunto_id = s.assunto_id;

  if (select count(*) from taxonomia.assuntos) <> (select count(*) from taxonomia.assuntos_new) then
    raise exception 'contagem de assuntos não bate após a cópia';
  end if;
  if (select count(*) from taxonomia.subassuntos) <> (select count(*) from taxonomia.subassuntos_new) then
    raise exception 'contagem de subassuntos não bate após a cópia';
  end if;

  drop table taxonomia.subassuntos;
  drop table taxonomia.assuntos;

  alter table taxonomia.assuntos_new rename to assuntos;
  alter table taxonomia.subassuntos_new rename to subassuntos;

  alter table taxonomia.subassuntos
    drop constraint subassuntos_assunto_id_fkey,
    add constraint subassuntos_assunto_id_fkey
      foreign key (assunto_id) references taxonomia.assuntos (assunto_id);

  create index assuntos_familia_id_idx on taxonomia.assuntos (familia_id);
  create index assuntos_disciplina_id_idx on taxonomia.assuntos (disciplina_id);
  create index subassuntos_familia_id_idx on taxonomia.subassuntos (familia_id);
  create index subassuntos_assunto_id_idx on taxonomia.subassuntos (assunto_id);

  if exists (select 1 from pg_roles where rolname = 'anon') then
    execute 'grant all on table taxonomia.assuntos to anon, authenticated, service_role';
    execute 'grant all on table taxonomia.subassuntos to anon, authenticated, service_role';
  end if;
end;
$mig$;
