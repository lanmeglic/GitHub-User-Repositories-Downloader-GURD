<h2>Overview</h2>

<p>This is a Python script that allows you to back up your GitHub repositories by cloning each repository to a local directory and then compressing the directory into a .zip file.</p>

<h2>Steps to Use the Script</h2>

<ol>
	<li>Create a personal access token on GitHub. To do this, go to your GitHub settings and click on "Developer settings" > "Personal access tokens". Then, click on "Generate new token" and follow the prompts to create a new token. Make sure to give the token the "repo" scope so that it can access your repositories.</li>
	<li>Open the script in a text editor and replace the following values:
		<ul>
			<li><code>your_username</code> with your GitHub username</li>
			<li><code>your_token</code> with the access token you just created</li>
			<li><code>backup_path</code> with the path to the directory where you want to store the backup files</li>
			<li><code>path_to_zip_file</code> with the path to the .zip file that you want to create</li>
		</ul>
	</li>
	<li>Save the modified script.</li>
	<li>Open a terminal window and navigate to the directory where the script is saved.</li>
	<li>Run the script by typing <code>python script_name.py</code>, where <code>script_name.py</code> is the name of the script file.</li>
	<li>The script will clone each of your repositories to the specified backup directory and then compress the directory into a .zip file. The backup files will be saved to the location you specified in step 2.</li>
</ol>

<h2>Makefile Code</h2>

<p>If you're using the Makefile to run the script, you can add the following code to your Makefile:</p>

<pre><code>backup:
python script_name.py
