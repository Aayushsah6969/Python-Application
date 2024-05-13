import tkinter as tk
import tkinter.simpledialog
from tkinter import messagebox

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note Taking App")
        
        self.notes = []

        self.note_listbox = tk.Listbox(root, width=50, height=20)
        self.note_listbox.pack(pady=10)

        self.load_notes()

        self.new_note_button = tk.Button(root, text="New Note", command=self.new_note)
        self.new_note_button.pack(side=tk.LEFT, padx=10)

        self.edit_note_button = tk.Button(root, text="Edit Note", command=self.edit_note)
        self.edit_note_button.pack(side=tk.LEFT, padx=10)

        self.delete_note_button = tk.Button(root, text="Delete Note", command=self.delete_note)
        self.delete_note_button.pack(side=tk.LEFT, padx=10)

        self.save_notes_button = tk.Button(root, text="Save Notes", command=self.save_notes)
        self.save_notes_button.pack(side=tk.LEFT, padx=10)

    def load_notes(self):
        try:
            with open("notes.txt", "r") as file:
                self.notes = [line.strip() for line in file.readlines()]
                self.update_listbox()
        except FileNotFoundError:
            pass

    def update_listbox(self):
        self.note_listbox.delete(0, tk.END)
        for note in self.notes:
            self.note_listbox.insert(tk.END, note)

    def new_note(self):
        note_text = tk.simpledialog.askstring("New Note", "Enter your note:")
        if note_text:
            self.notes.append(note_text)
            self.update_listbox()

    def edit_note(self):
        selected_index = self.note_listbox.curselection()
        if selected_index:
            selected_note = self.note_listbox.get(selected_index)
            edited_note = tk.simpledialog.askstring("Edit Note", "Edit your note:", initialvalue=selected_note)
            if edited_note:
                self.notes[selected_index[0]] = edited_note
                self.update_listbox()

    def delete_note(self):
        selected_index = self.note_listbox.curselection()
        if selected_index:
            self.notes.pop(selected_index[0])
            self.update_listbox()

    def save_notes(self):
        with open("notes.txt", "w") as file:
            for note in self.notes:
                file.write(note + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
