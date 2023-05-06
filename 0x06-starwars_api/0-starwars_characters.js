// #!/usr/bin/node

// const request = require('request');
// const filmId = process.argv[2];
// const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

// request(url, async (err, response, body) => {
//   if (err) {
//     console.log(err);
//   }
//   for (const characterId of JSON.parse(body).characters) {
//     await new Promise((resolve, reject) => {
//       request(characterId, (err, response, body) => {
//         if (err) {
//           reject(err);
//         }
//         console.log(JSON.parse(body).name);
//         resolve();
//       });
//     });
//   }
// });
#!/usr/bin/node


const request = require('request');
const Film_Id = process.argv[2];
const Movie_url = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + Film_Id,
  method: 'GET'
};

request(Movie_url, function (error, response, body) {
  if (!error) {
    const chars = JSON.parse(body).characters;
    print_Chars(chars, 0);
  }
});

function print_Chars (chars, index) {
  request(chars[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chars.length) {
        print_Chars(chars, index + 1);
      }
    }
  });
}