{ 
"module_spec": 
{
    "module_name": "DhcpDdns",
    "module_description": "DHPC-DDNS Service",
    "config_data": [
    { 
        "item_name": "interface",
        "item_type": "string",
        "item_optional": true,
        "item_default": "eth0"
    },

    { 
        "item_name": "ip_address",
        "item_type": "string",
        "item_optional": false,
        "item_default": "127.0.0.1" 
    },

    { 
        "item_name": "port",
        "item_type": "integer",
        "item_optional": true,
        "item_default": 53001 
    },
    {
        "item_name": "tsig_keys",
        "item_type": "list",
        "item_optional": true, 
        "item_default": [],
        "list_item_spec":
        {
            "item_name": "tsig_key",
            "item_type": "map",
            "item_optional": false,
            "item_default": {"algorithm" : "hmac_md5"},
            "map_item_spec": [ 
            {
                "item_name": "name",
                "item_type": "string",
                "item_optional": false,
                "item_default": ""
            },
            {
                "item_name": "algorithm",
                "item_type": "string",
                "item_optional": false,
                "item_default": ""
            },
            {
                "item_name": "secret",
                "item_type": "string",
                "item_optional": false,
                "item_default": ""
            }]
        }
    },
    {
        "item_name": "forward_ddns",
        "item_type": "map",
        "item_optional": true,
         "item_default": {},
         "map_item_spec": [ 
         {
            "item_name": "ddns_domains",
            "item_type": "list",
            "item_optional": false, 
            "item_default": [],
            "list_item_spec":
            {
                "item_name": "ddns_domain",
                "item_type": "map",
                "item_optional": false,
                "item_default": {},
                "map_item_spec": [ 
                { 
                    "item_name": "name",
                    "item_type": "string",
                    "item_optional": false,
                    "item_default": ""
                },

                { 
                    "item_name": "key_name",
                    "item_type": "string",
                    "item_optional": true,
                    "item_default": "" 
                },
    
                {
                    "item_name": "dns_servers",
                    "item_type": "list",
                    "item_optional": false, 
                    "item_default": [],
                    "list_item_spec":
                    {
                        "item_name": "dns_server",
                        "item_type": "map",
                        "item_optional": false, 
                        "item_default": {},
                        "map_item_spec": [ 
                        { 
                            "item_name": "hostname",
                            "item_type": "string",
                            "item_optional": true,
                            "item_default": ""
                        },
                        { 
                            "item_name": "ip_address",
                            "item_type": "string",
                            "item_optional": true,
                            "item_default": ""
                        },
                        { 
                            "item_name": "port",
                            "item_type": "integer",
                            "item_optional": true,
                            "item_default": 53 
                        }]
                    }
                }]
            }
        }]
    },

    {
        "item_name": "reverse_ddns",
        "item_type": "map",
        "item_optional": true,
         "item_default": {},
         "map_item_spec": [ 
         { 
            "item_name": "ddns_domains",
            "item_type": "list",
            "item_optional": false, 
            "item_default": [],
            "list_item_spec":
            {
                "item_name": "ddns_domain",
                "item_type": "map",
                "item_optional": false,
                "item_default": {},
                "map_item_spec": [ 
                { 
                    "item_name": "name",
                    "item_type": "string",
                    "item_optional": false,
                    "item_default": ""
                },

                { 
                    "item_name": "key_name",
                    "item_type": "string",
                    "item_optional": true,
                    "item_default": "" 
                },
    
                {
                    "item_name": "dns_servers",
                    "item_type": "list",
                    "item_optional": false, 
                    "item_default": [],
                    "list_item_spec":
                    {
                        "item_name": "dns_server",
                        "item_type": "map",
                        "item_optional": false, 
                        "item_default": {},
                        "map_item_spec": [ 
                        { 
                            "item_name": "hostname",
                            "item_type": "string",
                            "item_optional": true,
                            "item_default": ""
                        },
                        { 
                            "item_name": "ip_address",
                            "item_type": "string",
                            "item_optional": true,
                            "item_default": ""
                        },
                        { 
                            "item_name": "port",
                            "item_type": "integer",
                            "item_optional": true,
                            "item_default": 53 
                        }]
                    }
                }]
            }
        }]
    }],

    "commands": [
        {
            "command_name": "shutdown",
            "command_description": "Shuts down b10-dhcp-ddns module server.",
            "command_args": [
            {
                "item_name": "type",
                "item_type": "string",
                "item_optional": true,
                "item_default": "normal",
                "item_description": "values: normal (default), now, or drain_first"
            }
            ]
        }
    ]
  }
}

