import sys
import requests
from accounts.models import ListUser

class PersonaAuthenticationBackend(object):

	def authenticate(self, assertion):
		# 把判定数据发给Mozilla的验证服务
		data = {'assertion': assertion, 'audience': localhost}
		print('sending to mozilla', data, file=sys.stderr)
		resp = requests.post('https://verifier.login.persona.org/verify', data=data)
		print('got', resp.content, file=sys.stderr)

		# 验证服务时候有响应？
		if resp.ok:
			verification_data = resp.json()

			if verification_data['status'] == 'okay':
				email = verification_data['email']
				try:
					return self.get_user(email)
				except ListUser.DoesNotExist:
					return ListUser.objects.create(email=email)

	def get_user(self, email):
		return ListUser.objects.get(email=email)