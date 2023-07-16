package com.example.jpa.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
@Data
@AllArgsConstructor
@Entity
public class Member {

    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private long id;
    @Column
    private String name;
    @Column
    private int age;

    public Member(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public Member() {
    }
}
