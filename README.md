# №1

Плюсы реализации 1:
- Выполняет свою задачу
- С одного взгляда понятно, что делает код

Минусы реализации 1:
- Есть реализация чуть-чуть быстрее

Плюсы реализации 2:
- Выполняет свою задачу
- Чуть-чуть быстрее, чем реализация 1

Минусы реализации 2:
- Не сразу понятно, что делает функция

Понять, что реализация 2 быстрее, можно, посмотрев на ассемблированный код. Так как в ассембелере нет прямой операции взятия остатка компилятор будет искать обходные пути для выполнения. С другой же стороны операция not и операция and в реализации 2. Но разница вообще несущественна.

# №2
```cpp
class CycledFIFOBuffer
```
Реализован на списке и указателях на начало и конец, без лишних затрат по памяти/времени (если не учитывать, что можно было обойтись просто списком).

```cpp
class CycledFIFOBufferUsingPersistentStack
```
Реализован на двух классах персистентного стека, что, естественно, ухудшает как требуемую память, так и время работы. Но зато его можно доработать до персистентного класса при необходимости.

Файл comprasion.py содержит код для сравнения скорости работы обоих классов. В общем и целом можно сделать вывод, что если количество операций меньше, чем длина буффера, реализация 2 в ~3 раза дольше. Если же количество операций больше, чем длина буффера, это число начинает расти (при большом числе операций относительно длины, отношение скоростей достигает ~10).

# №3
Вообще говоря в условии не сказано, в каком порядке требуется сортировать массив, так что оптимальный код такой (кажется, быстрее чем за 0 времени нельзя):
```py
def func(a: list) -> list:
    return a
```
Если же имеется ввиду сортировка по возрастанию/убыванию/какому-либо другому компоратору, то многое зависит от более конкретной задачи. Так например сортировка подсчётом справляется за линейное время с небольшими числами, а при больших работает уже не столь хорошо. Если надо стабильно быструю сортировку, то подойдёт сортировка слиянием.
