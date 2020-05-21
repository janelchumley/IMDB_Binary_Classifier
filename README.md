## IMDB Binary Classifier 

#### Overview
You are a data scientist for a top movie studio. After a series of box office flops, the producers at your studio are starting to question their strategy and need some direction. You suggest a new approach - using data to determine what factors go into making a successful film. Luckily, you have a dataset of over 5000 films to mine for insights. Your producers ask you to spend some time analyzing the data and present a report detailing your findings, along with recommendations on how to revamp the studio’s strategy.

#### Data Dictionary (selected columns)

* num_critic_reviews - number of movie reviews written by critics
* num_user_reviews - number of movie reviews written by IMDB users
* num_users_voted - number of IMDB users that rated the film
* duration - the length of the film in minutes
* actor_n_facebook_likes - the number of likes on the actor’s Facebook page (we can assume this was measured before the movie was released)
* gross - the film’s gross revenue
* movie_score - the film’s rating on a 1-10 scale


#### Instructions
Because we want to be considerate of candidates’ time, we are asking that you spend 4 hours maximum on this assignment. The goal is to demonstrate how you think about an analytical problem and how you approach cleaning, visualizing, and analyzing a real dataset. As you have limited time, it may be beneficial to focus on a few quality, actionable insights over a thorough analysis that uses all the data. If you have ideas you don’t get to, it may be helpful to include in your submission a discussion of how you would have approached the problem with more time.

#### Contents of this repo
1. requirements.txt 
    
2. imdb_binary_classifier.ipynb
    
3. utils.py

4. imdb_5000.csv 

    
#### Prerequisites 

1. Create a virtual environment

    `python3 -m venv imdbenv`

2. Activate the new virtual environment

    `source imdbenv/bin/activate`
    
3. Install packages 

    `pip install -r requirements.txt`"

3. Create a Jupyter kernel for the new environment

    `python -m ipykernel install --user --name imdbenv --display-name "imdbenv"`

4. Start the Jupyter notebook server from your terminal 

    `jupyter notebook`

5. With the .ipynb file open in the browser, select Kernel then imdbenv from the dropdown.
