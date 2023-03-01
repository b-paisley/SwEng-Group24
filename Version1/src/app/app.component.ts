import { Component, OnDestroy } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { PiecesService } from './pieces.service';
import { takeUntil } from 'rxjs/operators';
import { Subject } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private pieces: PiecesService) {}

  title = 'SwEng-Group24';

  
  users: any;
  userCount = 0;

  destroy$: Subject<boolean> = new Subject<boolean>();


  getAllUsers() {
    this.pieces.getData().pipe(takeUntil(this.destroy$)).subscribe((users) => {
        this.users = users;
    });
  }

  ngOnDestroy() {
    this.destroy$.next(true);
    this.destroy$.unsubscribe();
  }
}
