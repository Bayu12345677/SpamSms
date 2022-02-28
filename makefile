package_1 = "ncurses-utils"
package_2 = "curl"
package_3 = "lynx"
package_4 = "figlet"
package_5 = "toilet"
package_6 = "wget"

setup:
	apt-get install $(package_1) -y
	apt-get install $(package_2) -y
	apt-get install $(package_3) -y
	apt-get install $(package_4) -y
	apt-get install $(package_5) -y
	apt-get install $(package_6) -y
run:
	chmod 0775 otp.sh
	./otp.sh
update:
	bash update.sh
	@echo
	@echo "successfully in the update"
	@echo "please type command cd. to update"
	@echo "tolong ketikan command (cd .) untuk mengupdate"
	@echo
