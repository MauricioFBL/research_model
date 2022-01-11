CREATE TABLE IF NOT EXISTS public.company
(
    id_company integer NOT NULL DEFAULT nextval('company_id_company_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default",
    company_premium boolean,
    company_size integer,
    ceo character varying(50) COLLATE pg_catalog."default" NOT NULL,
    avg_reputation double precision,
    total_ratings integer,
    ceo_score double precision,
    website character varying(150) COLLATE pg_catalog."default",
    culture_score double precision,
    work_life_balance double precision,
    stress_level double precision,
    CONSTRAINT company_pkey PRIMARY KEY (id_company)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.company
    OWNER to vmcjrdti;
--_________________________________________________________________________________________________________________________________________
-- Table: public.company_location

-- DROP TABLE IF EXISTS public.company_location;

CREATE TABLE IF NOT EXISTS public.company_location
(
    id_company_location integer NOT NULL DEFAULT nextval('company_location_id_company_location_seq'::regclass),
    company_id integer NOT NULL,
    location_id integer NOT NULL,
    CONSTRAINT company_location_pkey PRIMARY KEY (id_company_location, company_id, location_id),
    CONSTRAINT company_location_company_id_fkey FOREIGN KEY (company_id)
        REFERENCES public.company (id_company) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT company_location_location_id_fkey FOREIGN KEY (location_id)
        REFERENCES public.location (id_location) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.company_location
    OWNER to vmcjrdti;

--_________________________________________________________________________________________________________________________________________

-- Table: public.position_category

-- DROP TABLE IF EXISTS public.position_category;

CREATE TABLE IF NOT EXISTS public.position_category
(
    id_position_category integer NOT NULL DEFAULT nextval('position_category_id_position_category_seq'::regclass),
    category character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT position_category_pkey PRIMARY KEY (id_position_category)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.position_category
    OWNER to vmcjrdti;

--_________________________________________________________________________________________________________________________________________

-- Table: public.seniority

-- DROP TABLE IF EXISTS public.seniority;

CREATE TABLE IF NOT EXISTS public.seniority
(
    id_seniority integer NOT NULL DEFAULT nextval('seniority_id_seniority_seq'::regclass),
    seniority character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT seniority_pkey PRIMARY KEY (id_seniority)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.seniority
    OWNER to vmcjrdti;
--_________________________________________________________________________________________________________________________________________
-- Table: public.position

-- DROP TABLE IF EXISTS public."position";

CREATE TABLE IF NOT EXISTS public."position"
(
    id_position integer NOT NULL DEFAULT nextval('position_id_position_seq'::regclass),
    position_title character varying(150) COLLATE pg_catalog."default" NOT NULL,
    position_category_id integer,
    seniority_id integer,
    description text COLLATE pg_catalog."default" NOT NULL,
    modality character varying(50) COLLATE pg_catalog."default" NOT NULL,
    date_position timestamp without time zone NOT NULL,
    activate boolean NOT NULL,
    num_offers integer,
    salary_min integer,
    salary_max integer,
    salary integer,
    currency_id integer,
    remote boolean NOT NULL,
    location_id integer,
    english boolean NOT NULL,
    english_level character varying(50) COLLATE pg_catalog."default",
    position_url text COLLATE pg_catalog."default" NOT NULL,
    company_id integer,
    CONSTRAINT position_pkey PRIMARY KEY (id_position),
    CONSTRAINT position_company_id_fkey FOREIGN KEY (company_id)
        REFERENCES public.company (id_company) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT position_currency_id_fkey FOREIGN KEY (currency_id)
        REFERENCES public.currency (id_currency) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT position_location_id_fkey FOREIGN KEY (location_id)
        REFERENCES public.location (id_location) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT position_position_category_id_fkey FOREIGN KEY (position_category_id)
        REFERENCES public.position_category (id_position_category) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT position_seniority_id_fkey FOREIGN KEY (seniority_id)
        REFERENCES public.seniority (id_seniority) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."position"
    OWNER to vmcjrdti;

--_________________________________________________________________________________________________________________________________________

-- Table: public.position_skill

-- DROP TABLE IF EXISTS public.position_skill;

CREATE TABLE IF NOT EXISTS public.position_skill
(
    id_position_skill integer NOT NULL DEFAULT nextval('position_skill_id_position_skill_seq'::regclass),
    position_id integer NOT NULL,
    skill_id integer NOT NULL,
    CONSTRAINT position_skill_pkey PRIMARY KEY (id_position_skill, position_id, skill_id),
    CONSTRAINT position_skill_position_id_fkey FOREIGN KEY (position_id)
        REFERENCES public."position" (id_position) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT position_skill_skill_id_fkey FOREIGN KEY (skill_id)
        REFERENCES public.skill (id_skill) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.position_skill
    OWNER to vmcjrdti;
--_________________________________________________________________________________________________________________________________________
-- Table: public.location

-- DROP TABLE IF EXISTS public.location;

CREATE TABLE IF NOT EXISTS public.location
(
    id_location integer NOT NULL DEFAULT nextval('location_id_location_seq'::regclass),
    country character varying(50) COLLATE pg_catalog."default" NOT NULL,
    continent character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT location_pkey PRIMARY KEY (id_location)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.location
    OWNER to vmcjrdti;
--_________________________________________________________________________________________________________________________________________

--_________________________________________________________________________________________________________________________________________

--_________________________________________________________________________________________________________________________________________
