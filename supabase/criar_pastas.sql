-- Pastas (schemas) no Table Editor do Supabase
--
-- taxonomia/     _familias, _familias_composicao, disciplinas, assuntos, subassuntos
-- filtros/       bancas, banca_aliases, cargos, lista_orgaos, lista_orgao_aliases
-- questoes/      questoes
--
-- Como usar: SQL Editor → colar e Run.
-- Depois: Project Settings → API → Exposed schemas → incluir taxonomia, filtros, questoes.

-- ---------------------------------------------------------------------------
-- 1. Pastas
-- ---------------------------------------------------------------------------
create schema if not exists taxonomia;
create schema if not exists filtros;
create schema if not exists questoes;

comment on schema taxonomia is 'Árvore de conteúdo e famílias';
comment on schema filtros is 'Dimensões de prova: banca, cargo, órgão';
comment on schema questoes is 'Somente a tabela de questões';

-- ---------------------------------------------------------------------------
-- 2. Famílias no topo da pasta ( "_" ordena antes de "assuntos" )
-- ---------------------------------------------------------------------------
alter table if exists public.familias rename to _familias;
alter table if exists public.familias_composicao rename to _familias_composicao;

-- Se já estiverem em outro schema (reexecução parcial):
alter table if exists taxonomia.familias rename to _familias;
alter table if exists taxonomia.familias_composicao rename to _familias_composicao;

-- ---------------------------------------------------------------------------
-- 3. Mover tabelas
-- ---------------------------------------------------------------------------
alter table if exists public._familias            set schema taxonomia;
alter table if exists public._familias_composicao set schema taxonomia;
alter table if exists public.disciplinas          set schema taxonomia;
alter table if exists public.assuntos             set schema taxonomia;
alter table if exists public.subassuntos          set schema taxonomia;

alter table if exists public.bancas               set schema filtros;
alter table if exists public.banca_aliases        set schema filtros;
alter table if exists public.cargos               set schema filtros;
alter table if exists public.lista_orgaos         set schema filtros;
alter table if exists public.lista_orgao_aliases  set schema filtros;

alter table if exists public.questoes             set schema questoes;

-- ---------------------------------------------------------------------------
-- 4. API (PostgREST) e roles do Supabase
-- ---------------------------------------------------------------------------
grant usage on schema taxonomia, filtros, questoes to anon, authenticated, service_role;

grant all on all tables in schema taxonomia to postgres, service_role;
grant all on all tables in schema filtros   to postgres, service_role;
grant all on all tables in schema questoes  to postgres, service_role;

grant select on all tables in schema taxonomia to anon, authenticated;
grant select on all tables in schema filtros   to anon, authenticated;
grant select on all tables in schema questoes  to anon, authenticated;

grant all on all sequences in schema taxonomia to postgres, service_role;
grant all on all sequences in schema filtros   to postgres, service_role;
grant all on all sequences in schema questoes  to postgres, service_role;

alter default privileges in schema taxonomia grant all on tables to postgres, service_role;
alter default privileges in schema filtros   grant all on tables to postgres, service_role;
alter default privileges in schema questoes  grant all on tables to postgres, service_role;

alter default privileges in schema taxonomia grant select on tables to anon, authenticated;
alter default privileges in schema filtros   grant select on tables to anon, authenticated;
alter default privileges in schema questoes  grant select on tables to anon, authenticated;

-- ---------------------------------------------------------------------------
-- Client (depois de expor os schemas na API):
--   supabase.schema('taxonomia').from('_familias')
--   supabase.schema('filtros').from('bancas')
--   supabase.schema('questoes').from('questoes')
-- ---------------------------------------------------------------------------
