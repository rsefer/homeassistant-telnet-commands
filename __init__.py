import logging
import telnetlib

DOMAIN = "telnet_commands"
_LOGGER = logging.getLogger(__name__)

def setup(hass, config):

	def telnet_commands_service(call):
		_LOGGER.info('Received data', call.data)
		host = config['telnet_commands']['host'] or '192.168.0.2'
		port = config['telnet_commands']['port'] or 31339
		command = call.data.get('command', 'SETCH')
		value = call.data.get('value', '0612')
		telnet = telnetlib.Telnet(host, port)
		full_command = command + " " + value
		telnet.write(full_command.encode("ASCII") + b"\r")
		response = telnet.read_until(b"\r", timeout=0.5)

	hass.services.register(DOMAIN, 'send_command', telnet_commands_service)

	return True
