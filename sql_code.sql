CREATE TABLE gdp_states (
	state_code VARCHAR NOT NULL,
	year_ INTEGER NOT NULL,
	vp_gdp DECIMAL NOT NULL
);

CREATE TABLE startup_data (
	state_code VARCHAR NOT NULL,
	labels INTEGER ,
	founded_at INTEGER NOT NULL,
	age_first_funding_year DECIMAL,
	age_last_funding_year DECIMAL ,
	age_first_milestone_year DECIMAL,
	age_last_milestone_year DECIMAL,
	relationships INTEGER,
	funding_rounds INTEGER,
	funding_total_usd BIGINT,
	milestones INTEGER,
	is_CA INTEGER NOT NULL,
	is_NY INTEGER NOT NULL,
	is_MA INTEGER NOT NULL,
	is_TX INTEGER NOT NULL,
	is_otherstate INTEGER NOT NULL,
	is_software INTEGER NOT NULL,
	is_web INTEGER NOT NULL,
	is_mobile INTEGER NOT NULL,
	is_enterprise INTEGER NOT NULL,
	is_advertising INTEGER NOT NULL,
	is_gamesvideo INTEGER NOT NULL ,
	is_ecommerce INTEGER NOT NULL,
	is_biotech INTEGER NOT NULL,
	is_consulting INTEGER NOT NULL,
	is_othercategory INTEGER NOT NULL ,
	has_VC INTEGER NOT NULL ,
	has_angel INTEGER NOT NULL,
	has_roundA INTEGER NOT NULL,
	has_roundB INTEGER NOT NULL,
	has_roundC INTEGER NOT NULL,
	has_roundD INTEGER NOT NULL,
	avg_participants DECIMAL ,
	is_top500 INTEGER  ,
	reached_milestone INTEGER ,
	founded_first_funding_days_difference INTEGER,
	first_last_funding_days_difference INTEGER
);

--Joining startup_data and gdp_states
CREATE TABLE startup_alldata AS(
	SELECT
	gdp_states.state_code,
	gdp_states.year_,
	gdp_states.vp_gdp,
	startup_data.labels,
	startup_data.founded_at,
	startup_data.age_first_funding_year,
	startup_data.age_last_funding_year,
	startup_data.age_first_milestone_year,
	startup_data.age_last_milestone_year,
	startup_data.relationships,
	startup_data.funding_rounds,
	startup_data.funding_total_usd,
	startup_data.milestones,
	startup_data.is_CA,
	startup_data.is_NY,
	startup_data.is_MA,
	startup_data.is_TX,
	startup_data.is_otherstate,
	startup_data.is_software,
	startup_data.is_web,
	startup_data.is_mobile,
	startup_data.is_enterprise,
	startup_data.is_advertising,
	startup_data.is_gamesvideo,
	startup_data.is_ecommerce,
	startup_data.is_biotech,
	startup_data.is_consulting,
	startup_data.is_othercategory,
	startup_data.has_VC,
	startup_data.has_angel,
	startup_data.has_roundA,
	startup_data.has_roundB,
	startup_data.has_roundC,
	startup_data.has_roundD,
	startup_data.avg_participants,
	startup_data.is_top500,
	startup_data.reached_milestone,
	startup_data.founded_first_funding_days_difference,
	startup_data.first_last_funding_days_difference

	FROM gdp_states
	INNER JOIN startup_data
	ON gdp_states.state_code = startup_data.state_code AND 
		gdp_states.year_ = startup_data.founded_at
	
);