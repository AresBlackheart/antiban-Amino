from os import system as s
try:from colored import fore
except:s('pip install colored');from colored import fore
try:import AminoXZ
except:s('pip install AminoXZ');import AminoXZ
antiban="_(.a={}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{},=_(template-default.blog1.content,_locale=ar)_)_"
client = AminoXZ.Client()
s('cls')
error_color = fore.RED
successful_color = fore.GREEN
regular_color = fore.GREY_63
input_color = fore.DEEP_SKY_BLUE_2
print(fore.DARK_CYAN,"""

░█████╗░███╗░░██╗████████╗██╗██████╗░░█████╗░███╗░░██╗
██╔══██╗████╗░██║╚══██╔══╝██║██╔══██╗██╔══██╗████╗░██║
███████║██╔██╗██║░░░██║░░░██║██████╦╝███████║██╔██╗██║
██╔══██║██║╚████║░░░██║░░░██║██╔══██╗██╔══██║██║╚████║
██║░░██║██║░╚███║░░░██║░░░██║██████╦╝██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝	

	Made by Xsarz (@DXsarz)
	GitHub: https://github.com/xXxCLOTIxXx
	Telegram channel: https://t.me/DxsarzUnion
	YouTube: https://www.youtube.com/channel/UCNKEgQmAvt6dD7jeMLpte9Q
	Discord server: https://discord.gg/GtpUnsHHT4
	""",regular_color)

while True:
	try:client.login(email=input(f'{input_color}Email>> {regular_color}'), password=input(f'{input_color}Password>> {regular_color}'));print(successful_color,"Successful login", regular_color);break
	except Exception as error:print(error_color,'Fail login:\n',error,f'\n{regular_color}')

while True:
	try:comId = client.get_from_link(input(f"{input_color}Input community link>> "))['extensions']['community']['ndcId'];break
	except Exception as error:print(error_color, f"Fail:\n{error}\n", regular_color)

while True:
	print("\n1)Enable antiban\n2)Disable antiban\n")
	select = input(f"{input_color}Select an action>> {regular_color}")
	if select == '1':client.change_profile(comId=comId, content=antiban); print(successful_color,'Antiban enabled.\n',regular_color)
	elif select == '2':client.change_profile(comId=comId, content="@DXsarz"); print(successful_color,'Antiban disabled.\n',regular_color)
	else:print(error_color,f'\nChoose one of the items\n{regular_color}')