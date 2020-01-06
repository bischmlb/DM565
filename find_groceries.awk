BEGIN { FS=","
print "Produce to pick up from the store:"}
$3>1 {print $2}
/produce/ {print $2}
END {print "-----------"}
