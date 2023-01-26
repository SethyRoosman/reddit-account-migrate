this is the reddit sub and join thang

<h3> GET SUBREDDITS AND WRITE TO FILE</h3>
(assuming you are using zsh on Mac) type
<code>printenv</code>
to see your current environment variables. after that type
<code>nano ~/.zprofile</code>
add your client id, client secret, username, and pwd as variables in the form [var_name]="credentials"
you can find your client id and secret after creating a <a href="https://www.reddit.com/prefs/apps">reddit developer application</a>
for the redirect uri, put <code>http://localhost:8080</code>

replace env variables names in code with your new env variable names
