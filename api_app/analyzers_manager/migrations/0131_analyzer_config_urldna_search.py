from django.db import migrations
from django.db.models.fields.related_descriptors import (
    ForwardManyToOneDescriptor,
    ForwardOneToOneDescriptor,
    ManyToManyDescriptor,
    ReverseManyToOneDescriptor,
    ReverseOneToOneDescriptor,
)

plugin = {
    "python_module": {
        "health_check_schedule": None,
        "update_schedule": None,
        "module": "urldna.UrlDNA",
        "base_path": "api_app.analyzers_manager.observable_analyzers",
    },
    "name": "UrlDNA_Search",
    "description": "Search the [urlDNA.io](https://urldna.io) database to retrieve information about a domain, URL, or IP address.",
    "disabled": False,
    "soft_time_limit": 100,
    "routing_key": "default",
    "health_check_status": True,
    "type": "observable",
    "docker_based": False,
    "maximum_tlp": "GREEN",
    "observable_supported": ["ip", "url", "domain"],
    "supported_filetypes": [],
    "run_hash": False,
    "run_hash_type": "",
    "not_supported_filetypes": [],
    "model": "analyzers_manager.AnalyzerConfig",
}

params = [
    {
        "python_module": {
            "module": "urldna.UrlDNA",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "api_key_name",
        "type": "str",
        "description": "urlDNA.io API KEY.",
        "is_secret": True,
        "required": True,
    },
    {
        "python_module": {
            "module": "urldna.UrlDNA",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "scanned_from",
        "type": "str",
        "description": "The country from which the new scan is performed.",
        "is_secret": False,
        "required": False,
    },
    {
        "python_module": {
            "module": "urldna.UrlDNA",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "viewport_width",
        "type": "int",
        "description": "The screen width of the viewport used for the scan.",
        "is_secret": False,
        "required": False,
    },
    {
        "python_module": {
            "module": "urldna.UrlDNA",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "viewport_height",
        "type": "int",
        "description": "The screen height of the viewport used for the scan.",
        "is_secret": False,
        "required": False,
    },
    {
        "python_module": {
            "module": "urldna.UrlDNA",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "private_scan",
        "type": "bool",
        "description": "The visibility setting for the new scan: False will make it publicly visible and searchable.",
        "is_secret": False,
        "required": False,
    },
    {
        "python_module": {
            "module": "urldna.UrlDNA",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "user_agent",
        "type": "str",
        "description": "The browser User Agent used for the scan.",
        "is_secret": False,
        "required": False,
    },
    {
        "python_module": {
            "module": "urldna.UrlDNA",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "waiting_time",
        "type": "int",
        "description": "The waiting time for the page to load during the scan.",
        "is_secret": False,
        "required": False,
    },
    {
        "python_module": {
            "module": "urldna.UrlDNA",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "device",
        "type": "str",
        "description": "The device type used for scraping, either DESKTOP or MOBILE.",
        "is_secret": False,
        "required": False,
    },
    {
        "python_module": {
            "module": "urldna.UrlDNA",
            "base_path": "api_app.analyzers_manager.observable_analyzers",
        },
        "name": "urldna_analysis",
        "type": "str",
        "description": "The analysis type can either involve conducting a NEW_SCAN or performing a SEARCH within the urlDNA.io database.",
        "is_secret": False,
        "required": True,
    },
]

values = [
    {
        "parameter": {
            "python_module": {
                "module": "urldna.UrlDNA",
                "base_path": "api_app.analyzers_manager.observable_analyzers",
            },
            "name": "urldna_analysis",
            "type": "str",
            "description": "The analysis type can either involve conducting a NEW_SCAN or performing a SEARCH within the urlDNA.io database.",
            "is_secret": False,
            "required": True,
        },
        "analyzer_config": "UrlDNA_Search",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
        "for_organization": False,
        "value": "SEARCH",
        "updated_at": "2024-11-22T14:01:18.449928Z",
        "owner": None,
    }
]


def _get_real_obj(Model, field, value):
    def _get_obj(Model, other_model, value):
        if isinstance(value, dict):
            real_vals = {}
            for key, real_val in value.items():
                real_vals[key] = _get_real_obj(other_model, key, real_val)
            value = other_model.objects.get_or_create(**real_vals)[0]
        # it is just the primary key serialized
        else:
            if isinstance(value, int):
                if Model.__name__ == "PluginConfig":
                    value = other_model.objects.get(name=plugin["name"])
                else:
                    value = other_model.objects.get(pk=value)
            else:
                value = other_model.objects.get(name=value)
        return value

    if (
        type(getattr(Model, field))
        in [
            ForwardManyToOneDescriptor,
            ReverseManyToOneDescriptor,
            ReverseOneToOneDescriptor,
            ForwardOneToOneDescriptor,
        ]
        and value
    ):
        other_model = getattr(Model, field).get_queryset().model
        value = _get_obj(Model, other_model, value)
    elif type(getattr(Model, field)) in [ManyToManyDescriptor] and value:
        other_model = getattr(Model, field).rel.model
        value = [_get_obj(Model, other_model, val) for val in value]
    return value


def _create_object(Model, data):
    mtm, no_mtm = {}, {}
    for field, value in data.items():
        value = _get_real_obj(Model, field, value)
        if type(getattr(Model, field)) is ManyToManyDescriptor:
            mtm[field] = value
        else:
            no_mtm[field] = value
    try:
        o = Model.objects.get(**no_mtm)
    except Model.DoesNotExist:
        o = Model(**no_mtm)
        o.full_clean()
        o.save()
        for field, value in mtm.items():
            attribute = getattr(o, field)
            if value is not None:
                attribute.set(value)
        return False
    return True


def migrate(apps, schema_editor):
    Parameter = apps.get_model("api_app", "Parameter")
    PluginConfig = apps.get_model("api_app", "PluginConfig")
    python_path = plugin.pop("model")
    Model = apps.get_model(*python_path.split("."))
    if not Model.objects.filter(name=plugin["name"]).exists():
        exists = _create_object(Model, plugin)
        if not exists:
            for param in params:
                _create_object(Parameter, param)
            for value in values:
                _create_object(PluginConfig, value)


def reverse_migrate(apps, schema_editor):
    python_path = plugin.pop("model")
    Model = apps.get_model(*python_path.split("."))
    Model.objects.get(name=plugin["name"]).delete()


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ("api_app", "0063_singleton_and_elastic_report"),
        ("analyzers_manager", "0130_analyzer_config_nvd_cve"),
    ]

    operations = [migrations.RunPython(migrate, reverse_migrate)]
