<h2>Overview</h2>

<p>This is a Python script that allows you to back up your GitHub repositories by cloning each repository to a local directory and then compressing the directory into a .zip file.</p>

<h2>Steps to Use the Script</h2>

<ol>
	<li>Create a personal access token on GitHub. To do this, go to your GitHub settings and click on "Developer settings" > "Personal access tokens". Then, click on "Generate new token" and follow the prompts to create a new token. Make sure to give the token the "repo" scope so that it can access your repositories. MAKE SURE YOU HAVE GIT INSTALLED.</li>
	<li>Open the script in a text editor/visual studio and replace the following values:
		<ul>
			<li><code>username_youwantto_clone</code> with the username of the person you want to backup all the repos</li>
			<li><code>your_username</code> with your GitHub username</li>
			<li><code>your_token</code> with the access token you just created</li>
			<li><code>backup_path</code> with the path to the directory where you want to store the backup files. Make sure you use double backslashes.</li>
			<li><code>path_to_zip_file</code> with the path to .zip file that you want to copy repos to. Make sure you use double backslashes.</li>
		</ul>
	</li>
	<li>Save the modified script.</li>
	<li>Open a terminal window and navigate to the directory where the script is saved.</li>
	<li>Run the script by typing <code>python GURD.py</code></li>
	<li>The script will clone each of your repositories to the specified backup directory and then compress the directory into a .zip file. The backup files will be saved to the location you specified in step 2.</li>
</ol>
