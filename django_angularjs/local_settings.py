# Local dev server.
from settings import *


# Environment
# ===========
SITE_ID                             = 1
DEBUG                               = True
TEMPLATE_DEBUG                      = DEBUG

# Other django settings
# =====================
ADMIN_SECRET                        = ''

# Databases
# ==========
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'demo.db',
        'USER': 'demo',
        'PASSWORD': 'demo',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': '',
        }
}

LOCAL_INSTALLED_APPS = (
    # Development Utilities
    'devserver',
    'django_extensions',
    'debug_toolbar',
    'werkzeug',
    'lettuce.django',
    )

LOCAL_MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

# Emails
# =======
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Debug_toolbar & DevServer configs

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    }

DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # Not enabled by default
    'devserver.modules.ajax.AjaxDumpModule',
    #'devserver.modules.profile.MemoryUseModule', #Todo: debug guppy install
    'devserver.modules.cache.CacheSummaryModule',
    'devserver.modules.profile.LineProfilerModule',
    )

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    )
