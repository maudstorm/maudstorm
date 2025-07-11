from os import environ

SESSION_CONFIGS = [
<<<<<<< HEAD
    # dict(
    #     name='public_goods',
    #     app_sequence=['public_goods'],
    #     num_demo_participants=3,
    # ),
=======
    dict(
        name='task',
        app_sequence=['Task'],
        num_demo_participants=1,
    ),
    dict(
        name='Questionnaire',
        app_sequence=['Questionnaire'],
        num_demo_participants=1,
    ),
    dict(
        name='Instructions',
        app_sequence=['Instructions'],
        num_demo_participants=1,
        treatmentLogic = 'random',
        treatment = 'value',
    ),
    dict(
        name='Session',
        app_sequence=['InformedConsent','Instructions','Task','Questionnaire'],
        num_demo_participants=1,
        treatmentLogic='random',
        treatment = 'value', # Randomize between-subject treatment. 
    ),
>>>>>>> d14958d (Instructions and questionnaire: first update)
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

<<<<<<< HEAD
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
=======
PARTICIPANT_FIELDS = [
    'dbTrials',             # Database with all trial info
    'lPos',                 # Position of attributes 
    'iSelectedTrial',       # Trial selected for payment
    'bTimeout',             # Participant timed-out
    'sChoice',              # Decision of selected trial
    'sTreatmentLogic',           # Treatment name
    'sTreatmentFriendly',           # Treatment name
    'sTreatment',
]
SESSION_FIELDS = [
]
>>>>>>> d14958d (Instructions and questionnaire: first update)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

<<<<<<< HEAD
SECRET_KEY = '4693640272326'
=======
SECRET_KEY = '5401288888583'
>>>>>>> d14958d (Instructions and questionnaire: first update)
