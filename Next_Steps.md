## **Dockerfile, Kubernetes Deployment File and Code Versioning using GitHub**
In this video, we will be making our Docker file, our Kubernetes deployment file, and we will also

be doing our code versioning using GitHub.

First of all, let's create our Docker file.

So in the root directory you will create one Docker file.

And you can just copy paste the docker file from my GitHub repository.

Here I have given this docker file.

Just copy it and paste it here.

Okay now let me explain this docker file.

Now first of all we are using this Python 3.1 image right?

Then these are some essential environment variables although it's optional.

But it's a good practice to define these two environment variables.

Then inside our Docker container we will be creating one app work directory okay.

All the things will be inside this app work directory.

But what is this.

Basically we are installing some of the system dependencies.

But.

But since you are using OpenCV Python in the previous projects.

Also, you have defined the system dependencies inside a docker file.

There were less dependencies, but this time you are using OpenCV Python.

So some of some of the dependencies are required by OpenCV.

Also like your uh this lib one lib glib two lib Sm6 lib x6 lib render dev.

So these are required by OpenCV and otherwise if you if you have not defined these your app will not

work properly.

So make sure you copy the same docker file that I have given in the GitHub repo.

Okay, so it will depend.

It will install all the dependencies, including dependencies that are needed by OpenCV.

Right?

Then we are copying all the content.

We are copying all the content.

You can see all the contents here like your app, like your static templates, then your uh application,

then your docker file setup file requirements.txt.

We are copying all these from our GitHub repository, where we will upload it from there too inside

this work directory that we have defined.

Okay.

So we are copying all the contents from here to inside our work directory container.

Now how you installed all your application all your packages.

You write that command write pip install hyphen full stop in the first video of this project.

That is your project setup, right?

So we are doing the same thing here pip install hyphen full stop.

But why we have written this no catch dir.

So basically it will be a new restart okay.

It will be a new fresh restart that will not include the patched files.

Now where are the cached files.

So if you open your app you can see here are some cached files.

You can see Pi cache files.

So it will ignore this file and give you a restart.

And it will install all the setup.py all the things again.

Right now your app is running on 5000 port.

You can see app dot Pi.

It is running on 5000 port.

So you have to expose this particular port.

I'm exposing this port.

Now how you will run this app on the terminal.

Also in the previous video, you run your app using Python app dot Pi.

We are writing the same thing here.

So that is how your Docker file is made.

Let me give you a summary.

We are using this particular Python 3.1 parent image and these are some essential environment variables,

although it's optional and we are creating a work directory with the name app, then we are building

some dependencies that are required by OpenCV.

Okay, then we are copying all the contents from here to our app inside the Docker container that we

defined above only.

Okay, then we are installing all the requirements, all the packages using this pip install hyphen

full stop command.

Then we are exposing the flask port on which our app is running.

Then we are running our app using this particular command.

Well okay, now let's save this file.

Now we have to make the Kubernetes deployment file.

So for that we can just go here.

And this is your Kubernetes deployment.yaml.

Just copy it okay.

Now go to your VS code.

And let's create in the root directory.

Let's create Kubernetes deploy.

mint.ml okay.

And paste your content here.

Right.

Okay so you have seen in the previous projects also Kubernetes files basically contain two things.

Generally one is your deployment.

One is your service.

Okay.

Same thing is here.

One is your deployment, one is your service.

So let's name our deployment as LM ops app and make sure whatever name you give here give the same name

here in the app.

Here in the app.

Give the same name here in the app okay okay.

This is not necessary.

But here whenever whenever you have written app you have to give this LM ops app name okay.

Now number of replicas.

We want only one replica to keep our project simple.

You can keep it to keep maximum.

Keep it 2 to 3.

Okay.

Don't give too much replicas right now.

We have to give this.

What is this container port?

We will talk about this name and image also.

Don't worry.

But first of all let's talk about this container port.

We have to give the same port on which our flask app is running.

That is our 5000, right?

Then we will be defining environment variables inside our Kubernetes cluster.

You have seen the introduction video right?

So when we will make a Kubernetes cluster inside our Google Cloud Kubernetes Engine, we will inject

this API.

Because when we will be doing code versioning right.

I will do just now after this, uh, we will not push this environment file okay.

We will not push this environment file.

If this environment file is not there, how will we app recognize our API.

So we will use Kubernetes injection technique so directly we will inject our Kubernetes API into our

Kubernetes engine Kubernetes cluster.

And then we are fetching that API from our Kubernetes cluster using this segment of code okay we will

be defining one line of secret.

Inside of secret we will have one our API key okay.

So that's how we are fetching our Rock API key from our Kubernetes cluster.

Basically, we will first of all inject that into Kubernetes cluster.

You will see in the upcoming videos.

Then we will extract that, uh, rock API from that Kubernetes cluster only using this code.

Okay.

Now coming to the service part.

Give any service name.

Now in the app section you have to give the same name that you have given above.

LM ops app.

Okay.

Now protocol TCP protocol 80 and target port should be 5000.

Only the same port on which your flask is running.

Now comes the type.

Uh, basically there are three types of, uh, what you can set.

Service type one is cluster IP, one is node port, one is load balancer.

Since you are making your app public, the load balancer is the best.

When you are making your app private like it can only be accessed internally.

So cluster IP is the best.

Uh, for an external node port is good, but if you are making a fully public app, load balancer will

work best and our app is fully public, right?

We will make our app accessible from the internet.

So that's why we have set the type as load balancer.

Now coming to the this part this containers part.

First of all we have given the app name as Linux app.

Okay.

But what is this image.

What is this image.

Basically uh, in the upcoming videos when in the we have the story made somewhere.

Okay.

We have to when we will build our Docker image, we have to store that Docker image somewhere.

So where will be where we will be storing our image.

We have seen the introduction video.

We will be storing them inside our Google Artifact registry.

So this is the path of our Google Artifact registry from where it has to fetch that image.

Okay, so it is the path from where our Kubernetes have to fetch that image.

So this is the path of our Google Artifact registry.

Okay.

And from that Google Path registry okay.

It is fetching that LM ops app.

Latest image.

Okay.

We have to, uh, change this according to your, uh, configurations.

Okay?

It can be your region.

Okay.

Basically, it is the registry.

Then it is your project ID.

Okay, this is your project ID.

This is your artifact.

Artifact registry.

We can say artifact repo name.

And this is your image name.

Okay.

These are the four things.

First of all, uh, Google registry, Google cloud registry, this is your Google Project ID.

Okay, then this is your, uh, Google repo artifact repo name, and this is your image name.

We will talk about it in the upcoming videos also, but I'm telling it here only.

Basically, it is the path from where our Kubernetes have to fetch that particular image.

So we have given the Google Artifact Registry path okay.

Where our image is located inside this artifact registry.

So our Kubernetes is fetching that image and then deploying that image on this port 5000 whatever.

And we are accessing our API secrets grok API from our LM of secrets Grapes.

Okay.

So this is how your Kubernetes deployment is working.

Okay.

Now let's talk about the code versioning.

So for that we will be doing using GitHub only.

Okay.

So just I'm importing in the sorry I'm creating one file in the root directory only that is git ignore.

Basically here we will be setting some files that we don't want to uh push to our GitHub.

First of all we env okay.

Then the environment files we don't push our environment files.

Then your project management files also just copy its relative path and paste it here.

And I think the rest we can put right.

So open your terminal and let me clear the terminal.

Just go to your browser I hope you have installed the git CLI.

So first of all you have to install git.

Just search on the git install and install the git so that you can run git commands inside your uh vs

code.

Right now we have to create a repository.

Just go here and just create a new repository.

And let's name our repository as okay.

Let's name our repository as uh pretty detector.

And.

Just answer like this okay.

Let's keep it public and take this readme file.

We don't have to take it.

Just create the repository.

And now you have to run commands one by one.

First of all write this git init command.

Copy it, open your vs code, paste it here it will initialize empty repository.

Then you have to set the branch.

It can be main or it can be master depending on your GitHub repo.

Just copy whatever it is written on your.

Now we have to add the origin.

Basically we are connecting our local to our GitHub repo, so just paste it.

Start with clear screen.

Now you will write git add full stop.

Basically it is adding all the contents here from our local to our GitHub repo, except the files that

are inside this node.

Okay, you can see all the files are green and this venv this dot env and this project management file

are in green color.

Because these are not getting pushed, only the green ones are getting pushed.

Then I will write git commit git commit m and you can give any message I'm giving the message commit

okay.

And then you will write git push origin to main and press enter.

And you can see it is done.

Basically it will depend on your internet connection.

Just go here and just refresh and you can see all the files have been successfully pushed to your GitHub

repo.

Okay, so that was it for this video.

Now you can move on to your next video.

## **GCP Setup(Service Accounts, GKE, GAR)**

Hello everyone!

In this video we will be doing our Google Cloud setup.

So first of all, you have to open my GitHub repository that I have given in the resource section and

just open the full documentation.

Okay, now there are some checklists that you have to fulfill.

First of all your Docker file should be made, but we have done already the Kubernetes file should be

there.

We have done already a code versioning should be done.

We have done already in the previous video.

These all three things we have done already in the previous video okay.

So now comes the major part.

Basically we are doing the Google Cloud setup for this project.

So just open your GCP, make one account there.

You will get a $300 free credit.

Okay.

Just sign in into your account.

Okay.

So this we have opened our uh this Google cloud.

Okay.

First of all, you have to open and activate these six APIs, because if you are using Google Cloud

for the first time, these will be disabled.

But we have to enable them so that our project will not face any error.

Okay.

So just go here in the left pane select API and services and here select library okay.

And now you have to search for APIs one by one.

So first of all since we are using Kubernetes we will be enabling our Kubernetes engine.

So just search for it press enter.

And this is your Kubernetes Engine API.

And make sure you enable it.

In my case it is already enabled so I don't have to enable it again okay.

Let's go back.

Now let's check for another API.

Basically this is your container registry API.

When you have to store your Docker images somewhere in your Google Artifact registry, this API will

be used.

So just go here and paste it.

Press enter.

This is your Google Container Registry API and make sure you enable this also.

This is your Compute Engine API.

Basically, they deal with the uh, computation process of their VM instances.

Okay.

So that's why we have to enable these also.

So just search for it.

Press enter.

And you have to enable this also in my case it is enabled.

Now your cloud build API your cloud storage API your IAM API.

Okay.

Although some of the API are optional but it's better to enable them.

Okay.

This is also enabled cloud build API.

Now comes the Cloud Storage API.

Just search for it.

It's like Cloud Storage API.

Okay.

And make sure you enable this also.

Okay.

This is also enabled.

Now at last this is your iam API.

And iam API and this is your IAM API.

And make sure you enable this also.

So all the APIs are enabled.

Now go back to your home page now and this is also done now.

Now we have to create one Google Kubernetes Engine cluster and our artifact registry.

Okay first of all let's create a Kubernetes cluster.

So for creating your Kubernetes cluster just go to your Google Cloud home page and just search for GKE.

And you will see here Kubernetes Engine option.

Just click on this Kubernetes Engine option.

And just go to this.

On the left pane there is a cluster option.

Click on this cluster option and you have to create one cluster here okay.

Just create the cluster and it will ask for the name.

Let's give it some name.

Let's give it LM ops.

Okay.

The region.

Let's give it by default.

Region.

Let's keep it us central one only.

And make sure you select the standard tire only.

We don't want enterprise tire.

Basically these are enterprise tires for your companies level projects okay.

So let's keep it standard tire.

Now come to this fleet registration.

Just skip this fleet registration.

Come to this networking okay.

And just take this access using DNS.

Just take this and access using IPv4 address.

Also take this but don't take this.

Enable authorized networks.

Don't take this.

Keep it unticked okay.

We have we don't have to pick this okay.

Don't take I am again telling you.

Now come to advanced section.

No no we don't want anything.

Just create now okay okay.

Battery is low.

Let's create the cluster now.

So I think it will take around five minutes to create your cluster.

Okay.

So you can see currently it is cluster is being created.

So you will only move forward when this cluster is fully created.

Until it is getting created we can create our architecture industry.

Okay so you can search for Google Artifact registry.

Okay.

Just write artifact registry and just open this in new tab.

So these are your repository.

Let's create one repository.

Let's name it LM ops repo.

Like this.

Uh make sure you select the Docker and it is standard.

It is region.

Um Uh, let's give it region only and just select us central one, same as your Kubernetes.

Okay.

So I'm selecting US central one lower.

And.

Close this.

Let's rest of the things will be same okay.

And let's create your this repository also okay.

This will automatically gets created.

It will get created instantly.

But this Kubernetes cluster will take some time okay.

So you have to wait okay.

So we have done this also we have created Google Kubernetes cluster and we have created artifact registry

also.

Okay.

Now we have to create a service account because we want to give access to our Kubernetes.

We can't directly access okay because it is our personal account.

So we will give a service account to our when our deployment tool.

In our case it can be any deployment tool, any other CI CD deployment tool.

It can be your Circleci GitHub actions your GitLab, your Jenkins, any tool.

We will give a service account access so that our, uh, these CI CD tool can partially access our Kubernetes.

Okay.

On the left pane you will see one IAM admin.

Here only you will see service account okay.

This is service account.

Just click here and open this in new tab.

Okay.

Now create a new service account.

Okay.

Uh just give any name.

Uh, let's keep it pretty.

Anything.

Whatever you want to give.

Now just click on create and continue.

Now this is the main thing you have to give some permissions.

I think I have already defined the permission.

You have to give these five permissions okay.

You have to give these five permissions one by one.

First of all let's give the owner role.

I will search for owner and let's give the owner role.

Okay.

Add another role.

Then I have to give the, uh.

I think this that was storage object admin.

I have to give storage.

So basically we are giving partial access of these things, not the full access of our cloud storage

object admin.

Okay.

Just add another rule.

This is your storage object viewer.

Okay.

Then there is a artifact registry admin.

Uh, this is your artifact registry admin.

Let's try and search it and just go below Artifact Registry Administrator.

Now for our security, let's give Artifact Registry Writer also.

Artifact registry writer.

I think these were the five things.

Artifact registry writer, artifact registry admin owner, storage Object storage, object admin.

And you can see these are the five permissions owner, Object admin, Object viewer, registry admin,

registry writer.

Just continue.

Okay.

And just done okay.

Now search for your this service account.

Just click on this actions tab.

Just go to the Manage keys.

Basically we will be creating one access key.

So you will write Add key and you will write Create New Key.

And make sure you select the JSON format and just create your key okay.

It will download one JSON file.

You can see it now just open your VSCode.

Now open the folder where you have downloaded Did this JSON key and just copy it from here to your VSCode

and just change its name.

Okay.

You can just change its name to GCP key.

You can just change its name to GCP key dot JSON.

Okay.

Now we can't push this GCP key also to our GitHub.

So we have to include this also in your.

Gitignore.

So you have to write key dot JSON okay.

Like this.

Okay.

So yeah basically this GCP key dot JSON file will give you access to this particular project ID uh,

with those permission that we have already defined, that is your admin owner and your storage object

admin artifact registry admin okay.

So that's how you will access your, uh, Google Cloud specifically for Kubernetes and artifact registry.

Okay.

Because we want these two things only because we want to fetch the files from.

If you will see here this Kubernetes deployment file, we have to fetch this image from our, uh, that

particular, uh, artifact registry.

And we have to work with our Kubernetes engine also.

That's why we need these GCP.

Okay.

So if you will see the full documentation now we have downloaded the key okay.

We have to place the key in the root directory of our project.

And we have changed its name to GCP key.

And we have added it to our git ignore.

Okay so this was how you have done your Google Cloud setup.

Basically what we have done.

First of all uh we have we created Google Kubernetes cluster okay.

Uh, before that also we enabled six APIs that we need throughout our project.

Then we created one Google Kubernetes cluster.

Okay.

You will move to the next video only.

And only if your Kubernetes cluster has been successfully created.

You can see still your Kubernetes cluster is being created.

I will just refresh the page and let's see whether it has been created or not.

You can see it is still being created.

You will not move forward to the next video until this is fully created.

Okay.

Next we made our artifact repository repository with the name Lmax repo.

Right after that we created one service account and we created it.

Uh, we created service account with certain conditions, and then we created its access key.

And then we downloaded that access key in the JSON format and stored it inside our project.

We also don't want that key to our, uh, GitHub.

So that is why we included it in our gitignore file.

So that was it for this video.

Now you can access video only and only if you have been successfully selected.

You can see now it has been successfully created and we have gone green.

It means it is working with a new collaborator.

Next video.

## **Circle CI Pipeline Code**

Miniatura da aula
0:24 / 15:58
Hi everyone!

So in this video we will be writing our Circleci pipeline code.

First of all, what you have to do in the root directory only you will create one folder and folders

will be.py okay.

Basically when you will deploy your app using the Circleci okay.

When you will make a project on the Circleci website, the website automatically detects okay.

Website will automatically detect this folder.

So your name should be same as it is.

It should be dot circle CI.

Okay, just create this folder.

It is a folder.

Inside this you will create one file that is config dot config dot yml file.

Okay.

You can just copy the config.ml from my GitHub repository that I have given.

And I will be explaining the code here.

Okay, let me open this Kubernetes deployment file also side by side because we need this also.

Okay to explain.

First of all, what is this?

Let me explain one by one.

Your config.yml.

What is this?

Version 2.1.

Okay.

Basically, this is telling us that Circleci is using its version 2.1.

Circleci also has its version.

Okay.

So this is your CI version 2.1.

Okay.

Then comes your this part.

Executors or Docker executor.

Docker image cloud SDK latest working directory repo.

Okay.

Now what is this?

First of all our circleci is using Google Cloud SDK image okay.

It is using Google Cloud SDK image.

And how it's how this Google Cloud SDK image is being used.

Using Docker executor okay.

Basically it is fetching that image using the Docker, pulling that image and installing that image

in our directory.

Now why we choose this image?

Why we not used python image, ubuntu image or anything else.

Why use the Google Cloud image?

Because you will see throughout the project we have used this command gcloud.

GCloud.

Uh, you can see here also gcloud gcloud.

Okay.

So if you have installed the python okay.

If you have installed Python uh, image, then you have to install this gcloud CLI separately.

But if you are using Google Cloud image, this gcloud and all its dependencies are automatically by

default installed.

So that's why we are using this to reduce our work.

Okay.

Now what is this working directory okay.

As the name suggest only basically your code will run inside this directory okay.

The whole code will be inside this right now.

These are your jobs okay?

These will be your jobs, right?

First of all, your first job is checkout code.

Then your second job is build the Docker image.

Your third job is deployed to the Google Kubernetes Engine.

Basically, first of all, you will check out the GitHub repo.

Check out means basically, uh, what you can say.

Basically, you're pulling your code from GitHub into Docker container.

Okay.

Basically you are pulling your code from the GitHub, whatever you have uploaded on the GitHub directory

or GitHub repo, you are fetching that, you are pulling that and using it inside your container.

Because if you see docker file also, uh, basically it is copying all the things from that particular

uh source.

It can be GitHub or anything, and then it is storing it inside app.

So same thing is happening here only okay.

The checkout doing is checkout is doing the same thing.

It is pulling from GitHub and storing it inside Docker container.

That's why we are using Docker executor right now.

This is your second job.

Basically here we are building our Docker image and we are building and then we are pushing it to our

Google Artifact registry.

Okay.

So that's why we have, uh.

Uh, made it in this way.

First of all, we will be using the same Docker executor because for building and pushing the image,

we need Docker, right?

So that's why we need a Docker executor.

Okay.

Now what is this remote?

Uh, what is this remote Docker.

Okay.

Basically, this command will let you build Docker image inside this CI.

Okay.

If you want the permission to build images inside circle CI, you have to write this code that is set

up remote Docker.

Basically you are remotely accessing Docker inside your circle CI right.

Then you have two commands.

What is this command and what is this command okay.

Basically here are you what are you doing here?

You are authenticating and here you are building and pushing.

Okay?

here you are authenticating.

Then you are building and pushing right now.

What is this echo service key then?

Base64 encode.

Decode whatever it is.

Okay now you can see this GCP dot JSON okay.

Basically we will encode this.

We will import this GCP key.

Whatever content is there.

We will encode it into a format that is known as base64 okay.

We will encode it into base64 in the next video.

And we will store it in the environment variables inside Circleci and inside Circleci.

We will give it a name.

Okay.

Inside Circleci we have environment variables, so we will convert this GCP key into base64 format and

store it inside environment variables of Circleci.

Okay, so we are fetching here environment variable from CI okay.

We have stored already.

Suppose we have stored this The service key inside the circle K, which we will be doing in the next

video.

But let's suppose we have already done.

Okay, now what we are doing, we are fetching that service key and you have encoded right now we are

decoding and again converting it to JSON.

We are again converting it to JSON okay.

So why we have to do such long approach.

Why not directly.

Do we can't do directly.

Why?

Uh, because you can't push your GCP key to GitHub or any source code management.

First of all, we converted it into a circleci environment variables.

After that, we use that environment variables to recreate our failed.

Okay.

That's what we are doing here.

First of all we took this file okay.

From our local repository.

We converted it into a base64 image.

After converting into base64, it gets converted into a simple one liner code.

Okay.

So you can just copy it.

Then we pasted it inside one circle CI environment variables.

Okay, now it is inside our environment variables.

We did not expose it to any public repo.

Okay.

It is inside our private repo.

Private project.

Right from that environment variable.

We decoded it again to a GCP.

We decoded it again to a normal file.

So that's how we protected it from being exposed to a public platform.

Okay.

Now we have now our GCP project.

Now we use this GCP dot JSON to activate our service account.

Okay we use this service GCP activate service account.

Okay.

Then we configured it.

Then we configured it.

Okay.

Make sure you have to configure this part according to yourself.

Okay.

Whatever the reason you have make sure you change it to this.

In my case it is US central one.

So that's why I have given you central one.

You have to change it accordingly, right?

So this whole point was for authentication purpose that was to cover key from the environment variable

converted back into the file, decode it back into the JSON file.

Then we use that file to activate our service account.

And then we authorized sorry.

Then we authenticated our Docker using the particular region okay.

Make sure you change it according to your region.

In my case it is US central one.

Okay.

Now comes the main part of this job.

Now we are building and pushing the image.

First of all we will write docker build t.

Now what is this us central 1.....

Okay just come to your browser.

Just come to the uh g okay.

Just click on this repository okay.

If you open this live ops repo, if you open this repo.

And suppose if you copy this path, let me copy its path.

And if I open my VSCode.

code and let me show you here only.

Okay, let me show you here.

Like this.

Do you here if I paste this path.

This path is looking like.

If I place it above this only.

Okay, so this part is your registry.

Okay.

This is your project ID this much you can see.

We will place our project ID inside like environment variables.

So that's why we have written this.

So that it will automatically fetch from environment variables.

We don't have to write like this okay.

Then we have the loop.

We have passed the same thing.

Like you have to change it accordingly.

Uh, with respect to your Google Artifact Registry name.

Now the main thing is there whatever name you will give here.

Okay?

Make sure whatever name you are giving here, this will be your image name.

You can change it accordingly.

Okay, whatever.

But when you will change, Make sure you make the same changes in the Kubernetes deployment file.

Okay, just change the name here.

Also LM ops latest whatever you have given the name in the Config.yml, make sure to give the same naming

Kubernetes deployment or YAML file also.

Okay.

Now let's remove this.

This.

Now we have builded our Docker image.

Now we are pushing it.

Okay.

We are pushing with the same thing only like this.

As as we have built it, we are pushing with the same thing only.

Okay, easy.

Now comes the third job we have now our image.

Our image is inside our Google Artifact registry, right?

Again, we are doing the same thing.

We are using Docker executor.

First of all we are doing the checkout.

Okay.

Then we are setting up a remote docker because we want to run Docker commands, right.

So we have to give this permission set up remote Docker.

Then we have again authenticate with our Google Cloud because we need again we need this GCP key again

so that we can push.

So sorry.

We can deploy a push to image.

Okay.

So the same thing we have done here we are authenticating with our Google Cloud okay.

So I have already explained it.

So I will not explain it again.

Now comes this part.

This part now what is happening here.

First of all this is also part of configuration.

This configuration was for the Google Cloud.

And this configuration is for Google okay.

This is for the Google apps.

So first of all we are writing gcloud container cluster okay.

You have to pass the name here okay.

But we will be passing the cluster name inside the environment variables.

And we will be fetching that from environment variables only.

You will see in the next video.

That's why we have written the environment variable name that is GKE cluster.

Now you will be giving the region for which region you have created your Kubernetes cluster okay.

So you can see here Kubernetes cluster.

You can see it is location as US central one right.

So we will also give the computer compute region also in the environment variables.

That's why we have written the computer region.

Okay.

After that you will give a project in which project you have made your, uh this to Kubernetes cluster.

Okay.

You can get your Kubernetes sorry project IDs.

Just click on this whatever project you have and you will get the project ID here okay.

So this is your project ID right.

And we will also define the project ID inside our uh, environment variables of Circleci.

And after that we have authenticated our GCP and we have authenticated our Kubernetes.

Also in the main part is.

So first of all how you will deploy you will deploy using Kubernetes file.

So we are doing that only we are applying that file okay.

We are applying that file okay.

Okay.

So we are applying that file.

Now what is this command kubectl rollout.

Restart deployment.

Basically we are restarting the deployment.

So every time you would not be used.

Okay.

Now what is this.

Workflows version two deploy pipeline.

Okay.

Basically we are defining the workflow.

You have defined the jobs here, but you have not defined which pattern the jobs are to you.

Whether the checkout code should be first, should be first or should be first.

So you have not any pattern or the, uh, number.

Sorry, you have not defined pattern.

Or you can say the workflow in which each step has to be performed.

Right.

So we are defining only.

Okay.

So it means first of all you have to run the checkout code, right.

First of all you have to run the checkout code and you have to run this Docker image.

But Docker image will.

Be fulfilled.

It means if checkout code is successful, then only build docker image will remain the same for the

third node.

Uh, deploy to deploy to GKE will only run if your Docker image is successful.

We have found first of all checkout code, and after that Docker image will checkout successfully.

After that deployment will will run deploy to JC will run.

Docker image was successfully.

Okay.

So that's how you can hear a walkthrough of uh CI CD pipeline of CI.

Okay.

I think you are able to understand how it's working.

The main thing is here when you are building and pushing, when you are building and pushing.

Right.

And one more thing.

One more thing.

One more thing.

Uh, you have to change this also accordingly.

Okay, let me open the Kubernetes deployment file.

Uh, whatever you name, you will come here for the LM ops app.

Okay.

Make sure you copy the same name and you give the same name in the deployment section.

Okay.

Here.

Make sure you give the same name.

Okay.

And this should be your file name.

So in our case it is Kubernetes deployment.ml only.

But the main thing you have to change, uh, this is your LM ops app, whatever app you have defined

in the Kubernetes deployment.

YML.

The next thing you have to do, uh, is this whatever image, name, whatever repo name you have given

here, make sure to give the same repo name and same thing here also in this image section okay, of

your Kubernetes deployment YAML.

I hope you understand now.

So this was it for this video.

In this video basically we defined our circle CI pipeline code.

In the next video we will be running our circle CI pipeline.

We will be setting our environment variables and we will be running our app in the Google Kubernetes

Engine.

## **Full CI/CD Deployment of Application on GKE**


Miniatura da aula
21:26 / 21:27
Hello everyone!

In this video we will be doing our circle CI setup and we will be deploying our application on our Google

Kubernetes Engine.

In the previous video you have I have already explained the Google Kubernetes sorry circle CI code in

the previous previous video, we have done the GCP setup okay.

So first of all we will be converting this GCP key into base64 format okay.

So you will just copy this command okay.

Just open your VSCode and just open a git bash terminal okay.

If you have installed git cli git bash automatically comes pre-installed with it.

So you will search here and you will get git bash terminal okay.

And just write this command here.

Whatever you have copied.

Taking time okay.

Just paste it.

Make sure your GCP key in the root directory GCP key should be in the root directory and press enter.

Okay.

So this is in your base 64 format.

So this is your converted or you can say encoded GCP key.

Let me minimize it a bit.

You can just copy it.

But before that just make account on the website.

Go to the Circleci website.

Sign up there.

Okay.

Do the verification and just login into your account.

After you login into your account you will see something like this.

You have to create a project.

Go to the projects part okay.

And just create a new project okay.

And just click anything.

You can just write, build, test and deploy your software application.

Uh you can name it anything.

Let's name it LM apps.

Just click on set up a pipeline.

Okay.

So we are setting up a pipeline.

Let's name our pipeline as Build and test.

You can change it anything.

We will keep it default only okay.

Now you have to choose the repo, but before choosing, you have to connect it.

So you will get one option here.

In my case it is already connected with my GitHub.

But in your case you have to connect with your GitHub.

Basically it will ask for the GitHub authorization.

So you have to authorize it properly.

And then you can see the repo.

Same as me.

Okay.

Now what.

What was your repo name here.

That was celebrity detector question and answer.

So you have to search that only I will write celebrity detector.

Celebrity detector.

Question and answer.

Just select it and just click on set up your config.

But we have already set up our config in the previous video.

Okay we have not set up.

Basically we have not pushed.

You can see in this current GitHub directory we don't have our config.

Okay we can.

We created dot Circleci Config.yml.

Okay, so we have to push the code, this code cmd and just write git add git commit git push.

Okay, now come to your circleci again and just click on go back and again choose the repo.

Okay just choose the repo.

Uh celebrity detector question answer celebrity detector answer.

Where is that repo?

Celebrity detector.

Celebrity detector.

Question and answer.

Now you have to set up our config so it will automatically detect your config.

Okay.

So you can see it has automatically detected your config.yml file already.

It has detected you don't have to do anything okay.

Just go here and click on set up your triggers.

Now, what will be your trigger by default?

Uh circleci gives you one trigger, but as soon as you push something, as soon as you push something

to your GitHub directory, your pipeline will, uh, execute.

Okay.

Every time you push something, your pipeline will restart.

Right.

Or you can set any other events.

Also, we have set on all pushes.

You can, uh, set on something like this.

Like when run CI is added.

Okay.

But we are selecting all pushes.

It means whenever something is pushed to our GitHub repo, this pipeline should run.

Okay.

Now just click on this review and finish setup.

And we have to finish it.

Just finish it.

Okay.

You can just review.

We have given the name Build and test.

This will be our repo.

We are using the existing configuration file only.

And we are selecting all pushes.

Like whenever something is pushed we will execute our pipeline.

Okay, let's finish the setup.

Now.

Uh, just go to your projects.

So this was your LM ops.

Just go to the overview and just go to the settings.

Okay.

Now we will be defining our environment variables.

You can see on the left pane there is environment variables.

Just click on environment variables.

Now you have to add environment variables one by one.

Okay.

Just and the first environment variable your first environment variable will be just open your Circleci

Config.yml only.

You can see the first environment variable that you get is your gcloud service key.

So just copy its name as it is.

Paste it here in the name section.

Okay, don't add the dollar sign okay.

Don't add the dollar sign.

Just add the name gcloud service key.

Now what will be the value.

Value will be the format of our GCP dot JSON okay.

So open your bash terminal, where you have generated the base 64 format, and just copy it from here.

Don't add any space, okay?

Just copy from this last equal to like this and just copy from here.

Okay.

Till here.

Just copy it and make sure no extra spaces is there.

Paste it and add the environment variable.

Right then.

Now let's add another environment variable.

We have two environment variable okay.

What is your next environment variable.

Let's check let's check.

We have another environment variable that is your project ID.

So just copy the name as it is.

Copy it.

Paste it.

Now what is your project ID.

Just go to your GCP cloud.

Click on your project.

My project is generative language client.

Just copy this project ID okay.

Just copy it and just go to your circleci and paste it here.

Now add this environment.

Variables also add another environment variable to the VSCode.

Let me close this terminal and let me maximize it a bit.

You can create an environment variable for this also LM ops repo.

Okay.

You can just write a dollar.

Uh you can just write it with a environment variable also.

That is like dollar.

And you can just write artifact repo name anything.

But in our case we have not done.

But you can do.

Okay.

Now, uh, another environment variables are okay.

So this is your another environment variable.

That is your GKE cluster.

Copy it.

Paste it here.

Although I have already defined in the documentation also.

So these are your environment variables that you have to define okay.

Google service Google cloud service key done.

Project ID done GKE cluster.

We have defined GKE cluster.

Now what will be the value.

Let's go to a Kubernetes cluster and just open the cluster.

What is the name of the cluster?

Okay.

Just copy that name of the cluster.

Copy that.

Paste it here.

Okay I think it's not copied.

Just copy it.

Paste it here.

Okay.

Just add it.

Now what's the another thing that is compute region okay.

Google compute region.

Just copy it.

Add another variable Google compute region okay.

Here compute region where you are doing all the things.

Here you can just open the Kubernetes.

You can see the region when you are opening your cluster you are seeing the region.

So just click this select this region and paste it here and add it.

Open your VSCode and this one is project ID.

Project ID we have already defined right.

So no need.

Yeah.

I think we have defined all the environment variables.

When was your, uh, Google Cloud service key then?

GKE cluster, then Google compute region, Google project ID?

Okay, all those are done.

Okay, but suppose we have set the trigger as all pushes, but we I want to run the pipeline now.

I don't want to push anything.

I want to run the pipeline manually only.

So how you can run it manually.

Just go here, go to the back and just click on this pipelines.

Okay.

Here select in the all projects select your Linux project okay.

Select the branch.

Select the main okay.

Or you can just trigger the pipeline here.

Just choose a pipeline.

And our pipeline name was Build and Test.

Right.

Just select it and config source is this checkout source is also this.

And you have to run the Python.

A pipeline has started running manually.

Okay.

This pipeline will also run whenever you will, uh, make some changes in your GitHub and push that

changes to sorry whenever.

You will make some changes on the code and push that change in the GitHub.

So this your circle CI will automatically detect that there are some changes and it will automatically

trigger your pipeline.

Okay.

So I will show you that also don't worry.

So you can see our first stage is running.

First of all that is your checkout code.

So let's wait till all the stages are complete.

Then I will show you.

Okay, so you can see after some time our pipeline has been executed successfully and it has builded

and deployed our, uh, Docker image to our Google Kubernetes Engine.

Okay.

But let me give you a piece of advice.

Uh, when I was, uh, basically pasting the encoded GCP key into the environment variable section of

the circle CI.

Uh, I think I'm, I was not careful enough and just added a random space, okay, at the end or at

the front.

So that's why I got one error previously.

But you have to just be careful while copying the base64 encoded key so that there should be no extra

spaces at the front and back.

Also, okay, because they can cause error.

So that was a piece of advice.

Still, your app will not work.

Okay, you can just go to the LM ops and you have to go to the workload section.

Currently you are at the cluster section.

You have to go to the workload section.

And at the starting you will get.

This does not have minimum availability.

If you open this you will get the reason script LM of secret not found.

So we are getting this uh container configuration error because you can see if I open my Kubernetes

deployment file, Uh, let me minimize this terminal.

I have defined that.

I have a lot of secrets inside lm.

Of secrets.

I have a proc API key of a.

Kubernetes is not able to find that.

So that's why we are getting that error.

So how you can fix it?

Just go to your cluster.

Okay.

Just go to your cluster and open your cluster.

And you have to connect to your kubectl okay.

Just connect and click on Run in Cloud Shell.

Now just go to the documentation.

We have done this.

We have done this.

We have done this.

Basically uh we have to do first of all do the configurations.

So you have to change this command accordingly.

You have to give your own cluster name okay.

In our case it is LM ops.

So I will change the name accordingly.

Then you have to give the US central one.

You have to give the project ID here okay.

So I'm giving the same things here.

So Just copy it, okay?

Just keep it in VSCode for now.

I'm writing it here.

It's writing it here.

Our cluster name is, I think LM ops only.

Right?

Yeah, our cluster name is LM ops.

Right.

Let me open the.

Okay.

We have to authorize it.

Okay.

I think it will automatically do that.

Okay.

It has already done.

Okay.

It has automatically.

If I can show you, I can just take the screen bigger.

It has automatically done this command automatically.

GCloud container cluster get credential LM ops region us Central1 project gen lang okay.

It has automatically detected this command so we don't have to write it.

But in case it doesn't write this command.

So then you can change it that change that command accordingly okay.

And you have to just press enter.

Okay.

Because we have authorized it using the graphical only we got one option right.

Dialogue box we have click the authorize.

That's why we are getting that.

Are we get this command automatically right.

So yeah you can just remove it.

But if in your case you don't get this command.

So in that case you can just write it manually also okay.

Now we have to inject our API key inside our Kubernetes.

So for that we have one command to create secrets.

So you have to just copy this from VS code or any notepad.

Paste it here and you have to paste your API key here.

Okay there it is asking for your actual API key.

So just go to your environment variable.

Copy this API key.

Okay.

Just copy it from here.

Paste it here.

And now copy this whole code.

Let me cut it here and just go to the Kubernetes Engine and paste that command here Press enter and

you can see it is showing me that secrets has been created successfully.

It means it has injected those secrets inside my cluster.

Now, we will not test this, uh, container configuration error that we were facing.

Right?

So now what you can do, just go to the workflow and just go to the pipelines.

We have to again trigger the pipeline, just like the LM ops.

Okay.

Just trigger the pipeline.

It choose the pipeline.

We are choosing the build and test only.

We have only that pipeline only.

And just select the main branches and just run the pipeline.

So you have to again wait for some time till it gets deployed.

Let's wait because it will again do the checkout and it will again do the build Docker image.

Then it will deploy it.

So let's wait.

So as you can see your pipeline has been executed once again, successfully.

Now you have to come to your Kubernetes cluster.

Now come to the workloads.

And in the workloads.

Uh, we have to wait for some time.

Okay.

Just open this LM ops app.

Okay.

Uh, because billow billow, billow billow, or basically this was your previous pod.

Okay.

This was your previous app deployment.

We have, uh, there was error because we have not injected our LM of secret.

And this is your current application that has been deployed.

And it is.

Okay.

Okay.

Because in now we have injected but one piece of advice more okay.

When you will open your workload for the first time okay.

So you may see an error like this, like uh, minimum eligibility or something like that.

I don't know the perfect name for that error, but, uh, it will show something like that minimum minimum

eligibility or minimum eligibility like that.

Okay.

So you have to wait for some time.

Don't directly jump into the conclusions.

You have to wait for some time.

Wait patiently around five minutes.

If then it is also showing that same error after 5 to 10 minutes also.

Then you can call it a error.

Okay.

But wait for 5 to 10 times.

Because sometimes if you are running your Google Kubernetes Engine for the first time and you are on

the trial version, in trial version, you get a limited quota.

Okay.

So that's why it is using that limited resource to set up your Google Kubernetes Engine.

So it takes some time.

Okay.

So don't jump into the conclusion directly.

Now open your workloads and you will get one endpoint here.

Okay.

At the below you are getting the load balancer endpoint.

Just open this endpoint and you will see your application running here.

Okay.

You can see your application running here.

Let's check whether it's working fine or not.

Let's choose the file.

Uh let's give any file.

And let's detect the celebrity.

Okay, so it is showing us perfectly.

That is Salman Khan, actor producer, Indian being one of the most successful and highest paid actor

in Bollywood.

Okay, so we can check, uh, what is his age?

What is his age?

Let's ask.

And you can see Salman Khan was born on December 1965.

As of 2024, his age is 58 years old.

Okay.

Uh, you can do the same with other celebrities.

Also just detect the celebrity.

I think it is of Mahendra Singh Dhoni.

Okay.

Let's select another image.

Let's not.

It's taking time.

Okay.

I think the server time out.

Basically, I think it was due to my.

Internet connection error.

Okay.

Okay.

So this was due to my internet connection error.

So now you can just select any and just detect the celebrity.

Okay.

So this is Robert Downey Jr.

Oh and you can just ask anything about him like which role he plays in Marvel.

Okay.

Let's ask.

And it is giving me Robert Downey Jr plays the iron iconic role of Tony Stark.

Okay.

Our famous iron man.

Okay.

So yeah, that's how you deploy your project.

Now let's talk about the cleanup.

Because if you don't clean up, you will get unnecessarily charged and you will Uh, spend all of your

free credits that you give that you are, by default, given by the GCP.

Okay.

So just go to your clusters.

Okay.

Just click on this LM ops cluster or whatever you have formed.

Just delete it.

Okay.

And you have to give the name of the cluster for the successful deletion.

Just delete it.

Okay.

So it will automatically get deleted after some time.

And one more thing.

You have to delete this, uh, image repository.

Also your Docker image repository.

Just click this and just delete it and just delete.

Okay.

So you can see the repository has been deleted.

You can delete the service account also okay.

If you want you can delete the service account with service account we don't need that charge.

So it's it is properly up to you that if you want to delete the service account you can you don't want

to meet your goals.

Okay.

One more thing you can do.

Although you will not get charged for this also.

But you can just delete the project on the circleci.

Also, if you want.

Okay, you will not get charged or anything.

It's totally depends on you, but the only two things that you have to necessarily delete are your Kubernetes

cluster.

Okay, it is getting deleted.

You have to be in this page for some time and you have to delete your Docker repository, your artifact

repository, sorry.

Where your images are stored, Docker images are stored.

You have to delete that.

So what we have done in this video, basically we deployed our uh, application on our Google Kubernetes

Engine using the circle CI.

And we have also done the cleanup.

Okay.

Basically that was it about this project.

I hope you enjoyed and learned something new during the working of this project.

Thank you.

And you can learn more new things from other projects also.

So try the other projects also.

Okay?

Thank you.

Bye bye.