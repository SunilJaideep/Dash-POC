--
-- PostgreSQL database dump
--

-- Dumped from database version 14.7
-- Dumped by pg_dump version 14.7

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: dash_schema; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA dash_schema;


ALTER SCHEMA dash_schema OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: employee_dept; Type: TABLE; Schema: dash_schema; Owner: postgres
--

CREATE TABLE dash_schema.employee_dept (
    employee_id integer NOT NULL,
    department text,
    department_id integer
);


ALTER TABLE dash_schema.employee_dept OWNER TO postgres;

--
-- Name: employee_info; Type: TABLE; Schema: dash_schema; Owner: postgres
--

CREATE TABLE dash_schema.employee_info (
    employee_id integer NOT NULL,
    employee_name text,
    employee_salary numeric
);


ALTER TABLE dash_schema.employee_info OWNER TO postgres;

--
-- Name: login_meta_table; Type: TABLE; Schema: dash_schema; Owner: postgres
--

CREATE TABLE dash_schema.login_meta_table (
    username character varying NOT NULL,
    password character varying,
    created_at timestamp without time zone,
    modified_at timestamp without time zone,
    created_by character varying,
    modified_by character varying
);


ALTER TABLE dash_schema.login_meta_table OWNER TO postgres;

--
-- Name: dash_schemaemployee_dept; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dash_schemaemployee_dept (
    id integer NOT NULL,
    department character(50) NOT NULL,
    department_id integer NOT NULL
);


ALTER TABLE public.dash_schemaemployee_dept OWNER TO postgres;

--
-- Name: employee_dept; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee_dept (
    id integer NOT NULL,
    department character(50) NOT NULL,
    department_id integer NOT NULL
);


ALTER TABLE public.employee_dept OWNER TO postgres;

--
-- Data for Name: employee_dept; Type: TABLE DATA; Schema: dash_schema; Owner: postgres
--

COPY dash_schema.employee_dept (employee_id, department, department_id) FROM stdin;
1	IT	1
2	Delivery	2
3	Business	3
4	IT	1
5	IT	1
6	Delivery	2
7	Delivery	2
8	Business	3
\.


--
-- Data for Name: employee_info; Type: TABLE DATA; Schema: dash_schema; Owner: postgres
--

COPY dash_schema.employee_info (employee_id, employee_name, employee_salary) FROM stdin;
1	Sam	50000
2	Ram	70000
3	John	60000
4	Ron	20000
5	Manish	35000
6	Sidhanth	54000
7	Jagan	67000
8	Steve	56000
\.


--
-- Data for Name: login_meta_table; Type: TABLE DATA; Schema: dash_schema; Owner: postgres
--

COPY dash_schema.login_meta_table (username, password, created_at, modified_at, created_by, modified_by) FROM stdin;
admin	admin123	2022-02-13 08:00:00	2022-02-13 10:15:00	admin	admin
user	retested	2023-02-14 08:44:58.884902	2023-02-14 08:44:58.884902	user	user
sunil	password	2022-02-13 08:00:00	2022-02-13 10:15:00	sunil	sunil
ravi	testing	2023-02-14 10:09:52.367545	2023-02-14 10:09:52.367545	ravi	ravi
srikanth	test123	2023-02-14 10:10:09.783809	2023-02-14 10:10:09.783809	srikanth	srikanth
\.


--
-- Data for Name: dash_schemaemployee_dept; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dash_schemaemployee_dept (id, department, department_id) FROM stdin;
\.


--
-- Data for Name: employee_dept; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employee_dept (id, department, department_id) FROM stdin;
\.


--
-- Name: employee_dept employee_dept_pkey; Type: CONSTRAINT; Schema: dash_schema; Owner: postgres
--

ALTER TABLE ONLY dash_schema.employee_dept
    ADD CONSTRAINT employee_dept_pkey PRIMARY KEY (employee_id);


--
-- Name: employee_info employee_info_pkey; Type: CONSTRAINT; Schema: dash_schema; Owner: postgres
--

ALTER TABLE ONLY dash_schema.employee_info
    ADD CONSTRAINT employee_info_pkey PRIMARY KEY (employee_id);


--
-- Name: login_meta_table login_meta_table_pkey; Type: CONSTRAINT; Schema: dash_schema; Owner: postgres
--

ALTER TABLE ONLY dash_schema.login_meta_table
    ADD CONSTRAINT login_meta_table_pkey PRIMARY KEY (username);


--
-- Name: dash_schemaemployee_dept dash_schemaemployee_dept_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dash_schemaemployee_dept
    ADD CONSTRAINT dash_schemaemployee_dept_pkey PRIMARY KEY (id);


--
-- Name: employee_dept employee_dept_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee_dept
    ADD CONSTRAINT employee_dept_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

