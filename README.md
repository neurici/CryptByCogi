# CryptByCogi - Script Python pentru Criptarea/Decriptarea fisierelor

CryptByCogi este un criptor/decriptor de fișiere scris în python care criptează fișierele dvs. folosind Advanced Encryption Standard (AES). <a href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_(CBC)" target="_blank"><span style="color: blue">Modul CBC</span></a> este folosit la crearea codului AES, în care fiecare bloc este înlănțuit la blocul anterior din flux.

![123](https://user-images.githubusercontent.com/35377569/48672510-c9cd6580-eb5c-11e8-9f2e-1712c484a23b.jpg)

### Caracteristici
- [x] CryptByCogi are capacitatea de a genera o cheie de criptare aleatorie pe baza unei chei(parole) introdusă de utilizator.
- [x] CryptByCogi poate cripta și decripta cu succes tipurile de fișiere .txt și .docx.


### Cum se instalează și rulează în Linux
[1] Introduceți următoarea comandă în terminal pentru a descărca scriptul.

`git clone https://github.com/neurici/CryptByCogi`

[2] După descărcarea programului, introduceți următoarea comandă pentru a naviga în directorul descărcat și listarea conținutului

`cd CryptByCogi && ls`

[3] Instalarea dependențelor 

`pip3 install -r requirements.txt`

[4] Acum rulați scriptul cu următoarea comandă.

`python3 CryptByCogi.py`


### Cum se instalează și rulează în Linux
[1] Descărcați și rulați fișierul de instalare Python 2.7.x și Python 3.7 de la  <a href="https://python.org" target="_blank"><span style="color: blue">Python.org</span></a>
  - La instalarea Python 3.7, activați opțiunea <b>"Add Python 3.6 to PATH"</b>
  
[2] Descărcați și rulați fișierul de instalare Git de la <a href="https://git-scm.com/" target="_blank"><span style="color: blue">Git-scm.com</span></a>, alegeți Utilizați Git din Windows Cmd.

[3] După aceea, rulați Command Prompt și introduceți aceste comenzi:

```
git clone https://github.com/neurici/CryptByCogi
cd CryptByCogi
pip3 install -r requirements.txt
python3 CryptByCogi.py
```

### Demn de atentie 
1. Criptarea fișierelor imagine, audio și video folosind CryptByCogi poate duce la criptari care vor corupe fișierul. Asigurați-vă că aveți o copie de rezervă înainte de a încerca să criptați tipurile de fișiere menționate mai sus. (Nici o problemă cu tipurile de fișiere .txt și .docx) Vă rugăm să mă ajutați să remediez acest lucru.

2. Vă rugăm să vă amintiți/notați cheia de criptare pe care ați introdus-o. Dacă o uitați/pierdeți, nu veți mai putea să decriptați fișierele.

