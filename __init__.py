import logging
import telnetlib

DOMAIN = "telnet_commands"
_LOGGER = logging.getLogger(__name__)

def setup(hass, config):

	def telnet_commands_service(call):
		_LOGGER.info('Received data', call.data)
		command = call.data.get('command', 'SETCH')
		value = call.data.get('value', '0612')
		telnet = telnetlib.Telnet('192.168.0.12', 31339)
		full_command = command + " " + value
		telnet.write(full_command.encode("ASCII") + b"\r")
		response = telnet.read_until(b"\r", timeout=0.5)

	hass.services.register(DOMAIN, 'send_command', telnet_commands_service)

	return True
