#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

struct Street{
    int b, e, l, id;
    string name;
};
struct Car{
    int p;
    vector<int> path;
};
int main()
{
    int d, i, s, v, f;
    vector<Street> streets;
    vector<Car> cars;
    map<string,int> street_names;

    fstream InFile("in/a.txt");
    fstream OutFile("a_out.txt");

    // Input
    InFile >> d >> i >> s >> v >> f;
    for(i=0;i<s;i++){
        Street street = Street();
        InFile >> street.b >> street.e >> street.name >> street.l;
        street.id = i;
        streets.push_back(street);
        street_names.insert({street.name, i});
    }
    for(i=0;i<v;i++){
        Car car = Car();
        string street;
        InFile >> car.p;
        for(int j=0;j<car.p;j++){
            InFile >> street;
            int id = street_names[street];
            car.path.push_back(id);
        }
        cars.push_back(car);
    }
    InFile.close();

    // Logic


    // Output
    cout << "Hello World";
    return 0;
}
