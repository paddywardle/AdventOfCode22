#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <stdio.h>
#include <sstream>

std::vector<std::string> string_splitter(std::string str, char delimeter)
{
    std::vector<std::string> split_str;
    std::stringstream string_data(str);
    std::string val;

    while (std::getline(string_data, val, delimeter))
    {
        split_str.push_back(val);
    }
    return split_str;
}

int main()
{
    std::vector<char> stack_1 = {'F', 'R', 'W'};
    std::vector<char> stack_2 = {'P', 'W', 'V', 'D', 'C', 'M', 'H', 'T'};
    std::vector<char> stack_3 = {'L', 'N', 'Z', 'M', 'P'};
    std::vector<char> stack_4 = {'R', 'H', 'C', 'J'};
    std::vector<char> stack_5 = {'B', 'T', 'Q', 'H', 'G', 'P', 'C'};
    std::vector<char> stack_6 = {'Z', 'F', 'L', 'W', 'C', 'G'};
    std::vector<char> stack_7 = {'C', 'G', 'J', 'Z', 'Q', 'L', 'V', 'W'};
    std::vector<char> stack_8 = {'C', 'V', 'T', 'W', 'F', 'R', 'N', 'P'};
    std::vector<char> stack_9 = {'V', 'S', 'R', 'G', 'H', 'W', 'J'};

    std::vector<std::vector<char>> stack_list = {stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9};

    std::ifstream file("input.txt");
    std::string text;
    std::string answer="";
    
    while (std::getline(file, text))
    {

        std::vector<std::string> text_list = string_splitter(text, ' ');

        int num_crates = std::stoi(text_list[1]);
        int start_stack_index = std::stoi(text_list[3]) - 1;
        int finish_stack_index = std::stoi(text_list[5]) - 1;

        std::vector<char> starting_stack = stack_list[start_stack_index];
        
        for (int i=0; i<num_crates; i++)
        {
            std::vector<char> temp = stack_list[start_stack_index];

            stack_list[finish_stack_index].insert(stack_list[finish_stack_index].begin(), temp[0]);

            temp.erase(temp.begin());

            stack_list[start_stack_index] = temp;
        }

    }

    for (int i=0; i<stack_list.size(); i++)
    {
        answer += stack_list[i][0];
    }

    std::cout<<answer<<std::endl;
}