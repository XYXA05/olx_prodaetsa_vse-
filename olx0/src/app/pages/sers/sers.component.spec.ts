import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SersComponent } from './sers.component';

describe('SersComponent', () => {
  let component: SersComponent;
  let fixture: ComponentFixture<SersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SersComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
