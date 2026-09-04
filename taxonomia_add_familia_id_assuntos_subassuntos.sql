-- taxonomia — adiciona familia_id em assuntos e subassuntos
--
-- disciplinas já tem familia_id (FK para taxonomia._familias).
-- Este script:
--   1. cria a coluna (nullable) nas duas tabelas
--   2. preenche a partir de disciplinas (COMUM, ENGPRO e qualquer outra família já carregada)
--   3. aplica NOT NULL + FK
-- Idempotente: pode ser reexecutado se a coluna já existir.

begin;

alter table taxonomia.assuntos
  add column if not exists familia_id text;

alter table taxonomia.subassuntos
  add column if not exists familia_id text;

update taxonomia.assuntos a
set familia_id = d.familia_id
from taxonomia.disciplinas d
where a.disciplina_id = d.disciplina_id
  and (a.familia_id is distinct from d.familia_id);

update taxonomia.subassuntos s
set familia_id = a.familia_id
from taxonomia.assuntos a
where s.assunto_id = a.assunto_id
  and (s.familia_id is distinct from a.familia_id);

do $$
begin
  if exists (select 1 from taxonomia.assuntos where familia_id is null) then
    raise exception 'assuntos.familia_id ainda tem nulos; confira disciplinas.familia_id';
  end if;
  if exists (select 1 from taxonomia.subassuntos where familia_id is null) then
    raise exception 'subassuntos.familia_id ainda tem nulos; rode de novo depois de preencher assuntos';
  end if;
end $$;

alter table taxonomia.assuntos
  alter column familia_id set not null;

alter table taxonomia.subassuntos
  alter column familia_id set not null;

do $$
begin
  if not exists (
    select 1 from pg_constraint
    where conname = 'assuntos_familia_id_fkey'
      and conrelid = 'taxonomia.assuntos'::regclass
  ) then
    alter table taxonomia.assuntos
      add constraint assuntos_familia_id_fkey
      foreign key (familia_id) references taxonomia._familias(familia_id);
  end if;

  if not exists (
    select 1 from pg_constraint
    where conname = 'subassuntos_familia_id_fkey'
      and conrelid = 'taxonomia.subassuntos'::regclass
  ) then
    alter table taxonomia.subassuntos
      add constraint subassuntos_familia_id_fkey
      foreign key (familia_id) references taxonomia._familias(familia_id);
  end if;
end $$;

create index if not exists assuntos_familia_id_idx
  on taxonomia.assuntos (familia_id);

create index if not exists subassuntos_familia_id_idx
  on taxonomia.subassuntos (familia_id);

commit;
