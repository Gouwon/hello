# 1, 1, 2, 3, 5, 8

'''
while(TRUE) {
  input_value = as.integer(readline(prompt = "Input the number: "))
  if (input_value < 0) break
  
  x = 1
  y = 1
  n = input_value - 2
  result = paste(x, y)
  if (input_value == 0)
    print("The fibonacci sum of 0 is 0")
  else if (input_value == 1)
    result = paste(x)
  else if (input_value == 2)
    result = paste(x, y)
  else {
    for (i in 1:n) {
        z = x + y
        result = paste(result, z)
        print(result)
        x = y
        y = z 
    }
  }
  print(paste("The factorial of", input_value, "is", result))
}
'''

while (TRUE) {
  x = as.integer(readline(prompt="Inpit the count : "))
  if ( x <= 0 ) {
    print("End!")
    break
  }
  
  if ( x == 1 ) {
    print(0) 
    next
  }
  
  p0 = 0
  p1 = 1
  ret = paste(p0, p1)
  
  while( x > 2 ){
    p = p0 + p1
    p0 = p1
    p1 = p
    ret = paste(ret, p)
    x = x - 1
  }
  print(ret)
}



