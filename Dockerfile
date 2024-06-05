# Get the offical Golang docker image
FROM golang:1.22-bookworm

# Create a new workdirectory called lingolyrics
WORKDIR $GOPATH/src/LingoLyrics

# Copy contents to container image
COPY . ./

RUN go build -v -o /LingoLyrics

EXPOSE 8080

CMD ["/LingoLyrics"]