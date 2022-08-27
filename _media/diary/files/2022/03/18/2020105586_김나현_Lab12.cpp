#include <iostream>
#include <string>
#include "Text.h"
#include "FancyText.h"
#include "FixedText.h"
using namespace std;

/* 기초 1번 문제
class Base {
protected: //Base type
	void print_base() { cout << "Base" << endl; }
};

class Derived : private Base {
public:
	void print_derived() {
		Base::print_base();
		cout << "Derived" << endl;
	}
};

int main() {
	Base base;
	Derived derived;

	derived.print_derived();

	return 0;

}
*/

/* 기초 2~3번 문제
int main() {
	Text t1("Plain");
	t1.append("A");
	cout << t1.get() << endl;

	FancyText t2("Fancy", "<<", ">>", "***");
	t2.append("A");
	cout << t2.get() << endl;

	FixedText t3;
	t3.append("A");
	cout << t3.get() << endl;
	t1 = t2;

	return 0;
}
*/

/* 응용 1번 문제
class Polygon {
public:
	Polygon() {}
	Polygon(int point, float length) {
		mPoint = point;
		mLength = length;
	}
	~Polygon() {}
	virtual void calcPerimeter() { cout << "Perimeter: empty" << endl; }
	virtual void calcArea() { cout << "Area: empty" << endl; }
protected:
	int mPoint;
	double mLength;
};

class Rectangle : public Polygon {
public:
	Rectangle() {}
	Rectangle(int point, float length) : Polygon(point, length) {}
	~Rectangle() {}
	void calcPerimeter() override { cout << "Perimeter: " << mPoint * mLength << endl; }
	void calcArea() override { cout << "Area: " << mLength * mLength << endl; }
};

int main() {
	Polygon pol;
	Rectangle rec(4, 10);

	cout << "--- Polygon class ---" << endl;
	pol.calcPerimeter();
	pol.calcArea();

	cout << "--- Rectangle class ---" << endl;
	rec.calcPerimeter();
	rec.calcArea();

	return 0;
}
*/

/* 응용 2번 문제
class Polygon {
public:
	Polygon() {}
	Polygon(int point, float length) {
		mPoint = point;
		mLength = length;
	}
	~Polygon() {}
	virtual void calcPerimeter() { cout << "Perimeter: empty" << endl; }
	virtual void calcArea() { cout << "Area: empty" << endl; }
protected:
	int mPoint;
	double mLength;
};

class Rectangle : public Polygon {
public:
	Rectangle() {}
	Rectangle(int point, float length) : Polygon(point, length) {}
	~Rectangle() {}
	void calcPerimeter() override { cout << "Perimeter: " << mPoint * mLength << endl; }
	void calcArea() override { cout << "Area: " << mLength * mLength << endl; }
};

class Triangle : public Polygon {
public:
	Triangle() {}
	Triangle(int point, float length) : Polygon(point, length) {}
	~Triangle() {}
	void calcPerimeter() override { cout << "Perimeter: " << mPoint * mLength << endl; }
	void calcArea() override { cout << "Area: " << mLength * 0.5 * sqrt(3) * mLength * 0.5 << endl; }
};

class Circle : public Polygon {
public:
	Circle() {}
	Circle(int point, float length) : Polygon(point, length) {}
	~Circle() {}
	void calcPerimeter() override { cout << "Perimeter: " << 2 * 3.14 * mLength << endl; }
	void calcArea() override {
		cout << "Area: " << 3.14 * mLength * mLength << endl;
	}
};

int main() {
	Triangle tri(3, 10);
	Rectangle rec(4, 10);
	Circle cir(0, 5);
	cout << "--- Triangle class ---" << endl;
	tri.calcPerimeter();
	tri.calcArea();
	cout << "--- Rectangle class ---" << endl;
	rec.calcPerimeter();
	rec.calcArea();
	cout << "--- Circle class ---" << endl;
	cir.calcPerimeter();
	cir.calcArea();

	return 0;
}
*/

class Train {
public:
	Train() {}
	Train(int people) { mPeople = 0; }
	~Train() {}
	virtual int station(int takeOff, int takeOn) {}
protected:
	int mPeople;
};
class Ktx : public Train {
public:
	Ktx() : Train(0) {}
	Ktx(int people) : Train(people) {}
	~Ktx() {}
};

