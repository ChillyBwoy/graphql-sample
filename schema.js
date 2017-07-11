const fs = require('fs');
const path = require('path');
const fetch = require('isomorphic-fetch');
const {
  buildClientSchema,
  introspectionQuery,
  printSchema,
} = require('graphql/utilities');

const schemaPath = path.resolve(__dirname, 'schema.graphql');

fetch('http://localhost:8000/graphql/', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    },
    credentials: 'include',
    mode: 'cors',
    body: JSON.stringify({
      query: introspectionQuery
    }),
  })
  .then(response => response.json())
  .then(json => {
    fs.writeFileSync(schemaPath, printSchema(buildClientSchema(json.data)));
  });
