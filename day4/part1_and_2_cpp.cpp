#include <fstream>
#include <iostream>
#include <string>

int main()
{
    std::ifstream file("input.txt");
    std::string text;
    int total_part1=0;
    int total_part2=0;

    while (std::getline(file, text)){
        int comma_index = text.find(',');
        int end = text.length();
        std::string elf1 = text.substr(0, comma_index);
        std::string elf2 = text.substr(comma_index+1, end-comma_index);

        int elf1_dash = elf1.find('-');
        int elf2_dash = elf2.find('-');

        int elf1_end = elf1.length();
        int elf2_end = elf2.length();

        int elf1_1 = std::stoi(elf1.substr(0, elf1_dash));
        int elf1_2 = std::stoi(elf1.substr(elf1_dash+1, elf1_end-elf1_dash));

        int elf2_1 = std::stoi(elf2.substr(0, elf2_dash));
        int elf2_2 = std::stoi(elf2.substr(elf2_dash+1, elf2_end-elf2_dash));

        if (((elf1_1 <= elf2_1) && (elf1_2 >= elf2_2)) || ((elf1_1 >= elf2_1) && (elf1_2 <= elf2_2)))
        {
            total_part1 += 1;
        }

        if (((elf1_1 <= elf2_1) && (elf1_2 >= elf2_2)) || ((elf1_1 >= elf2_1) && (elf1_2 <= elf2_2)) || ((elf1_2 >= elf2_1) && (elf1_1 < elf2_1)) || ((elf2_2 >= elf1_1) && (elf2_1 < elf1_1)))
        {
            total_part2 += 1;
        }
    }
    std::cout<<"Part1: "<<total_part1<<std::endl;
    std::cout<<"Part2: "<<total_part2<<std::endl;
}