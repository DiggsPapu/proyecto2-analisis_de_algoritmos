#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <fstream>
#include <bits/stdc++.h>
#include "matplotlibcpp.h"

using namespace std;
using namespace std::chrono;
namespace plt = matplotlibcpp;

// Function to calculate binomial coefficient recursively
int binomialCoeff(int n, int k) {
    if (k > n)
        return 0;
    if (k == 0 || k == n)
        return 1;
    // Recursive Call
    return binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k);
}

int main() {
    int s = 35;
    std::vector<double> x, y, z;
    fstream file;
    file.open("../pares.txt", ios::in);
    if (!file){cout<<"no such file";}
    else{
        string line;
        while (std::getline(file, line)) {
            stringstream ss(line);
            string word;
            while (std::getline(ss, word, ',')) {
                x.push_back(stof(word));
                std::getline(ss, word, ',');
                y.push_back(stof(word));
            }
        }
    }
    std::ofstream outfile("values.txt", std::ios::app);
    // Prepare data.
    for(int i=0; i<x.size(); i++) {
        int n = x.at(i);
        int k = y.at(i);
        auto start = high_resolution_clock::now();
        binomialCoeff(n, k);
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<std::chrono::nanoseconds>(stop - start);
        outfile<<n;
        outfile << ",";
        outfile<<k;
        outfile<<",";
        outfile<<duration.count();
        outfile<<"\n";
    }
    outfile.close();
    return 0;
}
