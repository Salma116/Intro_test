const getAboutUsLink = require("./essai");
test("Returns about-us for english language", () => {
    expect(getAboutUsLink("en-US")).toBe("/about-us");
});