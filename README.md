1. Clone this repository into `/config/custom_components/`
2. Create a `telnet_commands.yaml` in `/config/` and add
```
  host: [IP ADDRESS]
  port: [POST || 31339]
```
3. Add `telnet_commands: !include telnet_commands.yaml` to `configuration.yaml`
