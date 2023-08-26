# Example of type(1)
print('********Type Check***********');
# int
print(type(1));
# int
print(type(-10))
# int
print(type(0));
# float
print(type(0.0));
# float
print(type(2.2));
# float
print(type(4E2));

# Example of Arithmetic
print('********Arithmetic***********');
print("Sum of two number ::", 10 + 3);

print('Subtraction ::', 10 - 2);

print(10 * 3);

print(10**3);

print(10 / 3);

print(10 // 3);

print(10 % 3);

# Basic Functions
print(pow(5, 2));

print(abs(-50));

print(round(5.46));

print(round(5.468, 2));
# Binary Conversion
print(bin(512));
# Hexadecimal
print(hex(512));

# ****** Converting Strings to Numbers
#age = input("How old are you?");
#age = int(age);
#pi = input("What is the value of pi?");
#pi = float(pi);

# Strings
print('********String***********');
print(type('Hello, How are you?'));
print('I\`m thristy');
name = 'Andrei Neagoie'
print(name[4])
print(name[:]);
print(name[1:]);
print(name[:1]);
print(name[-1]);
print(name[::1]);
print(name[::-1]);
print(name[0:10:2]);

print('Hi there ' + 'Timmy');

print(len('turtle'));

print(' I am alone '.strip());
# remove d
print('on an islandddd'.strip('d'));
# split in array
print('but life is good!'.split());

print('Help me'.replace('me', 'you'));

print('Need to make fire'.startswith('Need'));

print('and cook rice'.endswith('rice'));

print('bye bye'.index('e'));

print('still there?'.upper());

print('HELLO?!'.lower());

print('ok, I am done. Thanks'.capitalize());

print('oh hi there'.find('i'));

print('oh hi there'.count('e'));

# String Formatting
print('********String Formatting***********');
name1 = 'Dharmendra'
name2 = 'Raju'

print(f'Hello there {name1} and {name2}');
print('Hello there {} and {}'.format(name1, name2));
print('Hello there %s and %s' %(name1, name2));

# Palindrome check
print('********Palindrome***********');
word = 'reviver';
p = bool(word.find(word[::-1]) + 1);
print(p);

# Boolean
print('********Boolean***********');
print(bool(True));
print(bool(False));
print(bool(None));
print(bool(False));
print(bool(0));
print(bool(0.0));
print(bool([]));
print(bool({}));
print(bool(()));
print(bool(''));
print(bool(range(0)));
print(bool(set()));

# List
print('********List***********');
my_list = [1,2,'3',4,True];
print(len(my_list));
print(my_list.index('3'));
print(my_list.count(2));
