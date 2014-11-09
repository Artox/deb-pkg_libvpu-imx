#
# Regular cron jobs for the libvpu-imx6 package
#
0 4	* * *	root	[ -x /usr/bin/libvpu-imx6_maintenance ] && /usr/bin/libvpu-imx6_maintenance
