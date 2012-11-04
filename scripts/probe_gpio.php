#!/usr/bin/php

<?php
for ($i = 23; $i <= 25; $i++) {
	echo exec("cat /sys/class/gpio/gpio$i/value");
}
