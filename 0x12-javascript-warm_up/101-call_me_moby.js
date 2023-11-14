#!/usr/bin/node
exports.callMeMoby = function (n, theFunction) {
  let i;

  for (i = 0; i < n; i++) {
    theFunction();
  }
};
