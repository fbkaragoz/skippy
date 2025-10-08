#include <iostream>
#include <string>
#include <map>
#include <fstream>

/*
 * SECURITY WARNING: This encryption is NOT secure!
 * - Caesar cipher (shift by 1) is trivially broken
 * - Storing encrypted tokens in files is insecure
 * - Use proper secret management instead (environment variables, key vaults)
 * 
 * This tool is for educational purposes only.
 * DO NOT use in production environments.
 */

std::string encrypt(const std::string& input){
    // WARNING: This is NOT real encryption - just a Caesar cipher shift by 1
    std::string encrypted = input;
    for (char &c : encrypted) {
        c += 1;
    }
    return encrypted;
}

int main() {
    std::map<std::string, std::string> tokens;
    std::string tokenName, tokenValue;

    std::cout <<"Enter API token names and values."<< std::endl;
    std::cout<<"Enter without a value to pass the API you dont want to use."<<std::endl;
    std::cout<<"Enter a value to add a token."<<std::endl;
    std::cout<<"Enter \"done\" to finish."<<std::endl;

    std::string predefinedTokens[] ={"gpt_api_key", "youtube_api_key", "discord_api_key", "twitter_api_key"};

    for (const auto& predefinedTokenName: predefinedTokens){
        std::cout<<"Enter your token for " <<predefinedTokenName <<": ";
        std::getline(std::cin,tokenValue);

        if (tokenValue.empty()){
            std::cout << "skipping " << predefinedTokenName << std::endl;
            continue;
        }
        if (tokenValue == "done"){
            break;

        }
        tokens[predefinedTokenName] = tokenValue;

    }
    std::ofstream outfile("qwerty.txt");
    for (const auto&token : tokens){
        outfile << token.first << "=" << encrypt(token.second) << std::endl;
    }

    outfile.close();
    std::cout << "Tokens saved to encrypted_tokens.txt" << std::endl;
    return 0;
}