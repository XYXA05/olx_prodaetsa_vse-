import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnimatComponent } from './animat.component';

describe('AnimatComponent', () => {
  let component: AnimatComponent;
  let fixture: ComponentFixture<AnimatComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AnimatComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AnimatComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
