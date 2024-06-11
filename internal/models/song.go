// Data structure models to represent the song database entry
package models

type Song struct {
	ID      string        `bson:"_id,omitempty"`
	Title   string        `bson:"title,omitempty"`
	Lyrics  []interface{} `bson:"lyrics,omitempty"`
	Artists []interface{} `bson:"artists,omitempty"`
}
