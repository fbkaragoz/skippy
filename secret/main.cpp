#include <iostream>
#include <string>
#include <map>

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
    for (const auto& token : tokens) {
        std::cout << "token name: " <<token.first << " token value: " << token.second << std::endl;

    }
    return 0;
}