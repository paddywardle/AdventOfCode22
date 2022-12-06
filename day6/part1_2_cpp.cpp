#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>

int string_search(std::string str, int len)
{
    for (int i=0; i<str.length(); i++)
    {
        std::string current = str.substr(i, len);
        std::list<char> current_list;

        for (int j=0; j<current.length(); j++)
        {
            current_list.push_back(current[j]);
        }

        current_list.sort();
        current_list.unique();

        if (current_list.size() == len)
        {
            std::cout<<"Index: "<<i+len<<std::endl;
            break;
        }
    }
    return 0;
}

int main()
{
    std::ifstream file("input.txt");
    std::string text;

    while (file)
    {
        getline(file, text);
        string_search(text, 4);
        string_search(text, 14);
    }
}