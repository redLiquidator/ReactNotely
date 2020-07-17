in working with react, vscode is recommended rather than visual studio. 
create react project 'notelyreactapp': npx create-react-app notelyreactapp
run the project: npm start

 npm start
    Starts the development server.

  npm run build
    Bundles the app into static files for production.

  npm test
    Starts the test runner.

  npm run eject
    Removes this tool and copies build dependencies, configuration files
    and scripts into the app directory. If you do this, you can’t go back!


000000000000000000000000000000000000000000000000000000000000000000000000000000000000

redux npm install redux --save (state management)
redux-thunk npm install redux-thunk --save (should work with redux. asynchronous requestcodep챙ㄷ)
react-redux npm install react-redux --save
connected-react-router npm install connected-react-router --save
history npm install history --save
node-sass npm install node-sass --save
bootstrap npm install bootstrap --save
react-router-dom npm install react-router-dom --save
npm install rimraf --save

Question**npm install --save : the meaning of "--save" ?

As of npm 5.0.0, installed modules are added as a dependency by default, 
so the --save option is no longer needed. The other save options still exist and are 
listed in the documentation for npm install.

It won't do anything if you don't have a package.json file. 
Start by running npm init to create one. Then calls to npm install --save or npm install --save-dev or 
npm install --save-optional will update the package.json to list your dependencies.

