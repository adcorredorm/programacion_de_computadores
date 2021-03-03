/*
Para 2 números previamente proporcionados,
calcule e imprima el resultado de las 4 operaciones básicas (suma, resta, multiplicación y división) 
*/

#include <iostream>

int main() {
  int num1 = 51;  
  int num2 = 23;

  int suma = num1 + num2;
  int resta = num1 - num2;
  int multi = num1 * num2;
  int div = num1 / num2;

  std::cout << "El resultado de la suma es: " << suma << std::endl;

  std::cout << "El resultado de la resta es: " << resta << std::endl;

  std::cout << "El resultado de la multiplicacion es: " << multi << std::endl;

  std::cout << "El resultado de la division es: " << div << std::endl;
}
