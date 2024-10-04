#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

//Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // loop over all voters
    for(int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

//Update vote totals given a new vote
bool vote(string name)
{
    //TODO
    // to add a vote for a candidate if he has a vote that has his name
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes++;
            return true;
        }
    }

    // if the vote name doesn't match the name of a particular candidate
    // we do nothing
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name))
        {
            return false;
        }
    }

    return 0;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    //TODO
    int big;
    // get the biggest number of votes
    for (int i = 0; i < candidate_count ; i++)
    {
        if (candidates[0].votes < candidates[i].votes)
        {
            big = candidates[i].votes;
        }

        else
        {
            big = candidates[0].votes;
        }

    }

    // search for the candidates who have the highest number of votes
    // that we got from the previous steps
    for(int k = 0; k < candidate_count; k++)
    {
        if (candidates[k].votes == big)
        {
           printf("%s\n", candidates[k].name);
        }
    }
}