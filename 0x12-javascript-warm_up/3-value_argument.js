#!/usr/bin/node
const [_, __, arg] = process.argv; /* The underscores indicate the vars are ignored knowingly */

if (!arg) {
  console.log('No argument');
} else {
  console.log(arg);
}
