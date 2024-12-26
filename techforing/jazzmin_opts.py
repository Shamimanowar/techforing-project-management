from django.utils.translation import gettext_lazy as _
from django.conf import settings


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": _("TechForing Portal"),

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": _("TechForing Limited"),

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": _("TechForing Limited"),

    # Logo to use for your site, must be present in static files, used for brand on top left
    # "site_logo": "techforingltd_logo.jpeg",
    "site_logo": None,

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "techforing.png",

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": 'techforing.png',

    # Welcome text on the login screen
    "welcome_sign": _("Welcome to the Techforing Limited Admin Panel"),

    # Copyright on the footer
    "copyright": "Shamim Anowar",

    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string 
    "search_model": ["project_management.User", ],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    # #############
    # # User Menu #
    # #############

    # # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://techforing.com/findus", "new_window": True, 'icon': 'fas fa-rocket'},
        {"model": "project_management.user"}
    ],

    # #############
    # # Side Menu #
    # #############

    # # Whether to display the side menu
    "show_sidebar": True,

    # # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": ["auth"],

    # # Hide these models when generating side menu (e.g auth.user)
    # "hide_models": [],

    # # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [
        "project_management.User",
        "project_management.Project",
        "project_management.ProjectMember",
        "project_management.Task",
        "project_management.Comment",
        ],

    # # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # # for the full list of 5.13.0 free icon classes
    "icons": {
        "project_management.User": "fas fa-users",
        "project_management.Project": "fas fa-project-diagram",
        "project_management.ProjectMember": "fas fa-users-cog",
        "project_management.Task": "fas fa-tasks",
        "project_management.Comment": "fas fa-comments",
    },
    # # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",


}

JAZZMIN_UI_TWEAKS = {
    "accent": "accent-navy",
    "layout_boxed": False,

    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": True
}