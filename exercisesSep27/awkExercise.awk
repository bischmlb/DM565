BEGIN{FS=","
sumT1=0
sumT2=0
sumT3=0
individual=0
tests=3
redTeam=0
blueTeam=0
greenTeam=0
print "Name    Average"
print "----    -------"}

{
  if (!($3==-1))
  {
  individual=($3+$4+$5)/tests
  print $1, individual
  }
  else
  {
    individual=($4+$5)/(tests-1)
    print $1, individual
  }
}

{
  if ($2 == "Red")
  {
    redTeam=redTeam+individual
  }
  else if ($2 == "Green")
  {
    greenTeam=greenTeam+individual
  }
  else if ($2 == "Blue")
  {
    blueTeam=blueTeam+individual
  }
}

{ if (!($3==-1)) sumT1=sumT1+$3} ## because we have 1 line with -1, so dont add
{ if (!($4==-1)) sumT2=sumT2+$4}
{ if (!($5==-1)) sumT3=sumT3+$5}

END{ print "------------"
print "Average", "Test 1", sumT1/(NR-1) ## hardcode because retard
print "Average", "Test 2", sumT2/NR
print "Average", "Test 3", sumT3/NR
print "------------"
print "Average, Red: ", redTeam/3
print "Average, Blue: ", blueTeam/2
print "Average, Green: ", greenTeam/3}
